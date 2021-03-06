from django.db.models import Q
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse,reverse_lazy
from django.utils.timezone import make_naive
from django.views.generic import TemplateView,ListView,CreateView,DeleteView,UpdateView

from webapp.models import Article, Project
from webapp.forms import ArticleForm, BROWSER_DATETIME_FORMAT, SimpleSearchForm
from .base_view import FormView as CustomFormView



class IndexView(ListView):
    template_name = 'article/index.html'
    context_object_name = 'articles'
    paginate_by = 3
    paginate_orphans = 0

    def get_context_data(self, *, object_list=None, **kwargs):
        form = SimpleSearchForm(data=self.request.GET)
        if form.is_valid():
            search = form.cleaned_data['search']
            kwargs['search'] = search
        kwargs['form'] = form
        return super().get_context_data(object_list=object_list, **kwargs)

    def get_queryset(self):
        data = Article.objects.all()
        form = SimpleSearchForm(data=self.request.GET)
        if form.is_valid():
            search = form.cleaned_data['search']
            if search:
                data = data.filter(Q(description__icontains=search) | Q(maxdescription__icontains=search))

        return data.order_by('-publish_at')

@login_required
def article_mass_action_view(request):
    if request.method == 'POST':
        ids = request.POST.getlist('selected_articles', [])
        if 'delete' in request.POST:
            Article.objects.filter(id__in=ids).delete()
    return redirect('index')



class ArticleView(TemplateView):
    template_name = 'article/article_view.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        pk = self.kwargs.get('pk')
        article = get_object_or_404(Article, pk=pk)

        context['article'] = article
        return context

class ArticleCreateView(LoginRequiredMixin,CreateView):
    model = Article
    template_name = 'article/article_create.html'
    form_class = ArticleForm

    def form_valid(self, form):
        project = get_object_or_404(Project, pk=self.kwargs.get('pk'))
        types = form.cleaned_data.pop('types')
        article = form.save(commit=False)
        article.project = project
        article.users = self.request.user
        article.save()
        article.types.set(types)
        return redirect('project_view',pk=project.pk)




class ArticleUpdateView(PermissionRequiredMixin,UpdateView):
    template_name = 'article/article_update.html'
    form_class = ArticleForm
    model = Article
    permission_required = 'webapp.change_article'

    def has_permission(self):
        project = self.get_object()
        return super().has_permission()  and self.request.user in project.users.all()

    def get_initial(self):
        return {'publish_at': make_naive(self.object.publish_at)\
            .strftime(BROWSER_DATETIME_FORMAT)}

    def get_success_url(self):
        return reverse('article_view', kwargs={'pk': self.object.pk})



class ArticleDeleteView(PermissionRequiredMixin,DeleteView):
    template_name = 'article/article_delete.html'
    model = Article
    permission_required = 'webapp.delete_article'

    def get(self, request, *args, **kwargs):
        return self.delete(request, *args, **kwargs)

    def has_permission(self):
        article = self.get_object()
        return super().has_permission() and self.request.user in article.users.all()

    def get_success_url(self):
        return reverse('project_view',kwargs={'pk':self.object.project.pk})




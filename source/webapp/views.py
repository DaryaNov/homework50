from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponseNotAllowed
from django.urls import reverse
from django.utils.timezone import make_naive
from django.views.generic import View, TemplateView, FormView

from webapp.models import Article
from webapp.forms import ArticleForm, BROWSER_DATETIME_FORMAT
from .base_view import FormView as CustomFormView


class IndexView(View):
    def get(self, request):
        is_admin = request.GET.get('is_admin', None)
        data = Article.objects.all()
        return render(request, 'index.html', context={
            'articles': data
        })

class ArticleView(TemplateView):
    template_name = 'article_view.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        pk = self.kwargs.get('pk')
        article = get_object_or_404(Article, pk=pk)

        context['article'] = article
        return context


class ArticleCreateView(CustomFormView):
    template_name = 'article_create.html'
    form_class = ArticleForm

    def form_valid(self, form):
        self.article = form.save()
        return super().form_valid(form)

    def get_redirect_url(self):
        return reverse('article_view', kwargs={'pk': self.article.pk})



class ArticleUpdateView(FormView):
    template_name = 'article_update.html'
    form_class = ArticleForm

    def dispatch(self, request, *args, **kwargs):
        self.article = self.get_object()
        return super().dispatch(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['article'] = self.article
        return context

    def get_initial(self):
        initial = {}
        for key in 'description', 'maxdescription', 'status':
            initial[key] = getattr(self.article, key)
        initial['publish_at'] = make_naive(self.article.publish_at)\
            .strftime(BROWSER_DATETIME_FORMAT)
        initial['types'] = self.article.types.all()
        return initial

    def form_valid(self, form):
        self.article = form.save()
        return super().form_valid(form)

    def get_success_url(self):
        return reverse('article_view', kwargs={'pk': self.article.pk})

    def get_object(self):
        pk = self.kwargs.get('pk')
        return get_object_or_404(Article, pk=pk)

def article_delete_view(request, pk):
    article = get_object_or_404(Article, pk=pk)
    if request.method == 'GET':
        return render(request, 'article_delete.html', context={'article':article})
    elif request.method == 'POST':
        article.delete()
        return redirect('index')
    else:
        return HttpResponseNotAllowed(permitted_methods=['GET', 'POST'])
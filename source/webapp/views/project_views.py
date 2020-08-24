from django.views.generic import CreateView,ListView, DetailView , FormView
from django.core.paginator import Paginator
from django.http import HttpResponseNotAllowed
from django.shortcuts import render, redirect, get_object_or_404,reverse
from webapp.models import Project, Article
from webapp.forms import ArticleProjectForm



class Index_View(ListView):
    model = Project
    context_object_name = 'projects'
    template_name = 'project/index_project.html'

    def get_objects(self):
        return Project.objects.order_by('-newdate_at')


class ProjectView(DetailView):
    template_name = 'project/project_view.html'
    model = Project
    paginate_projects_by = 2
    paginate_projects_orphans = 0

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        pk = self.kwargs.get('pk')
        project = get_object_or_404(Project, pk=pk)

        context['project'] = project
        return context


class ArticleProjectCreateView(CreateView):
    model = Project
    template_name = 'project/project_create.html'
    form_class = ArticleProjectForm

    def form_valid(self, form):
        article = get_object_or_404(Article, pk=self.kwargs.get('pk'))
        project = form.save(commit=False)
        project.article = article
        project.save()
        return redirect('project/project_view', pk=article.pk)

    # def form_valid(self, form):
    #     article = get_object_or_404(Article, pk=self.kwargs.get('pk'))
    #     form.instance.article = article
    #     return super().form_valid(form)




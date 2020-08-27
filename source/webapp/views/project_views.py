from django.views.generic import CreateView,ListView, DetailView , FormView, UpdateView, DeleteView
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

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        pk = self.kwargs.get('pk')
        project = get_object_or_404(Project, pk=pk)

        context['project'] = project
        return context



class ArticleProjectCreateView(CreateView):
    model = Project
    form_class = ArticleProjectForm
    template_name = 'project/project_create.html'

    def get_success_url(self):
        return reverse('project_view', kwargs={'pk': self.object.pk})



class ProjectUpdateView(UpdateView):
    model = Project
    template_name = 'project/project_update.html'
    form_class = ArticleProjectForm

    def get_success_url(self):
        return reverse('project_view', kwargs={'pk': self.object.pk})


class ProjectDeleteView(DeleteView):
    model = Project
    template_name = 'project/project_delete.html'
    context_object_name = 'project'

    def get_success_url(self):
        return reverse('index_project')






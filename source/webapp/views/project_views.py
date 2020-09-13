from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin, UserPassesTestMixin
from django.views.generic import CreateView,ListView, DetailView , FormView, UpdateView, DeleteView
from django.core.paginator import Paginator
from django.http import HttpResponseNotAllowed
from django.shortcuts import render, redirect, get_object_or_404,reverse

from accounts.admin import User
from webapp.models import Project, Article
from webapp.forms import ArticleProjectForm, ProjectUserForm


class Index_View(ListView):
    model = Project
    context_object_name = 'projects'
    template_name = 'project/index_project.html'

    def get_objects(self):
        return Project.objects.order_by('-newdate_at')


@login_required
def project_mass_action_view(request):
    if request.method == 'POST':
        ids = request.POST.getlist('selected_projects', [])
        if 'delete' in request.POST:
            Article.objects.filter(id__in=ids).delete()
    return redirect('index_project')



class ProjectView(DetailView):
    template_name = 'project/project_view.html'
    model = Project

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        pk = self.kwargs.get('pk')
        project = get_object_or_404(Project, pk=pk)

        context['project'] = project
        return context


class ArticleProjectCreateView(PermissionRequiredMixin,CreateView):
    model = Project
    form_class = ArticleProjectForm
    template_name = 'project/project_create.html'
    permission_required = 'webapp.add_project'



    def has_permission(self):

        return super().has_permission()

    def get_success_url(self):
        return reverse('project_view', kwargs={'pk': self.object.pk})

    # def test_func(self):
    #     return self.request.user.has_perm('webapp.add_project') and \
    #            self.request.user in self.get_object().users.all()




class ProjectUpdateView(PermissionRequiredMixin,UpdateView):
    model = Project
    template_name = 'project/project_update.html'
    form_class = ProjectUserForm
    permission_required = 'webapp.can_change_project'


    def has_permission(self):
        project = self.get_object()
        return super().has_permission() and self.request.user in project.users.all()

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['users'] = User
        return context

    def get_success_url(self):
        return reverse('project_view', kwargs={'pk': self.object.pk})


class ProjectDeleteView(UserPassesTestMixin,DeleteView):
    model = Project
    template_name = 'project/project_delete.html'
    context_object_name = 'project'

    def get_success_url(self):
        return reverse('index_project')

    def test_func(self):
        return self.request.user.has_perm('webapp.delete_project') or \
            self.get_object().users == self.request.user







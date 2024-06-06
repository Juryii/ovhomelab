from django.shortcuts import get_object_or_404, render
from django.views.generic import (
    ListView,
    DetailView,
    UpdateView,
    DeleteView,
    CreateView,
)
from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.exceptions import PermissionDenied
from django.urls import reverse_lazy
from project.models import Projects
from .forms import ProjectCreateForm, ProjectEditForm


# Create your views here.


class ProjectAccessMixin:
    def get_object(self, queryset=None):
        obj = get_object_or_404(Projects, pk=self.kwargs["pk"])
        if not obj.user_has_access(
            self.request.user
        ):  # Добавьте вашу логику проверки доступа здесь
            raise PermissionDenied("У вас нет доступа к этому проекту.")
        return obj


class ProjectCreateView(LoginRequiredMixin, CreateView):
    model = Projects
    form_class = ProjectCreateForm
    template_name = "project/project_create.html"
    success_url = reverse_lazy("project:projects")

    def form_valid(self, form):
        form.instance.created_by = self.request.user
        return super().form_valid(form)

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        kwargs["user"] = self.request.user  # Передаем текущего пользователя в форму
        return kwargs


class ProjectsListView(LoginRequiredMixin, ProjectAccessMixin, ListView):
    login_url = "/login/"
    model = Projects
    template_name = "project/projects_list.html"
    context_object_name = "projects"

    def get_queryset(self):
        user = self.request.user
        return Projects.objects.filter(users=user) | Projects.objects.filter(
            created_by=user
        )


class ProjectDetailView(LoginRequiredMixin, ProjectAccessMixin, DetailView):
    login_url = "/login/"
    model = Projects
    template_name = "project/project_detail.html"
    context_object_name = "project"


class ProjectEditView(LoginRequiredMixin, ProjectAccessMixin, UpdateView):
    model = Projects
    form_class = ProjectEditForm
    template_name = "project/project_edit.html"
    success_url = reverse_lazy("project:projects")


class ProjectDeleteView(LoginRequiredMixin, DeleteView):
    model = Projects
    success_url = reverse_lazy("project:projects")
    template_name = "project/project_confirm_delete.html"

    def get_object(self, queryset=None):
        # Получаем объект проекта
        obj = super().get_object(queryset)
        # Проверяем, имеет ли текущий пользователь право на удаление проекта
        if not obj.user_has_access_delete(self.request.user):
            # Если у пользователя нет доступа к проекту для удаления, возбуждаем 403 ошибку
            raise PermissionDenied("У вас нет прав для удаления этого проекта.")
        return obj

    def get_success_url(self):
        return reverse_lazy("project:projects")


def custom_permission_denied(request, exception):
    return render(request, "403.html", status=403)


def custom_page_not_found(request, exception):
    return render(request, "404.html", status=404)


def index(request):
    "return index.html"
    return render(request, "project/index.html")

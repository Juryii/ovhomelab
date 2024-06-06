from django import forms
from django.contrib.auth.models import User
from .models import Projects


class ProjectEditForm(forms.ModelForm):
    class Meta:
        model = Projects
        fields = ["project_name", "project_description", "users"]
        labels = {
            "project_name": "Название проекта",
            "project_description": "Описание проекта",
            "users": "Пользователи у которых будет доступ к проекту",
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields["users"].widget = forms.CheckboxSelectMultiple()
        self.fields["users"].required = False
        self.fields["users"].queryset = User.objects.all()
        self.fields["users"].queryset = User.objects.exclude(
            pk=self.instance.created_by.pk
        )


class ProjectCreateForm(forms.ModelForm):
    class Meta:
        model = Projects
        fields = ["project_name", "project_description", "users"]
        labels = {
            "project_name": "Название проекта",
            "project_description": "Описание проекта",
            "users": "Пользователи, у которых будет доступ к проекту",
        }

    def __init__(self, *args, **kwargs):
        self.user = kwargs.pop("user")  # Получаем пользователя из kwargs
        super().__init__(*args, **kwargs)
        self.fields["users"].required = False
        self.fields["users"].widget = forms.CheckboxSelectMultiple()
        self.fields["users"].queryset = User.objects.exclude(pk=self.user.pk)

    def clean_project_name(self):
        project_name = self.cleaned_data["project_name"]
        if Projects.objects.filter(project_name=project_name).exists():
            self.add_error(
                "project_name",
                "Проект с таким названием уже существует. Измените наименование проекта",
            )
        return project_name

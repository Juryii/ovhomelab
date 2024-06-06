from django.contrib import admin
from .models import Projects


class ProjectAdmin(admin.ModelAdmin):
    filter_horizontal = (
        "users",
    )  # Это позволяет отображать список пользователей с помощью чекбоксов в админке


# Register your models here.
admin.site.register(Projects, ProjectAdmin)

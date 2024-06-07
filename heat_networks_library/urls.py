""" импорт модулей """

from django.urls import path

from .views import index

app_name = "heat_networks_library"

urlpatterns = [path("", index, name="index")]

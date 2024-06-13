""" импорт модулей """

from django.urls import path
from .views import index, HeatNetworksLibraryListView, PipeCreateView

app_name = "heat_networks_library"

urlpatterns = [
    # path("", index, name="index"),
    path("", HeatNetworksLibraryListView.as_view(), name="index"),
    path("add-pipe/", PipeCreateView.as_view(), name="add_pipe"),
]

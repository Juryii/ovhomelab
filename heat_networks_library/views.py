""" импорт модулей"""

from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import (
    CreateView,
    ListView,
    # DetailView,
    # UpdateView,
    # DeleteView,
    # CreateView,
)
from django.urls import reverse_lazy
from heat_networks_library.forms import PipeCreateForm
from ovhomelab.utils import SuperuserRequiredMixin
from heat_networks_library.models import Pipe


# Create your views here.
def index(request):
    "return index.html"
    return render(request, "heat_networks_library/index.html")


class HeatNetworksLibraryListView(LoginRequiredMixin, ListView):
    login_url = "/login/"
    model = Pipe
    template_name = "heat_networks_library/pipe_list.html"
    context_object_name = "pipes"


class PipeCreateView(SuperuserRequiredMixin, CreateView):
    login_url = "/login/"
    model = Pipe
    form_class = PipeCreateForm
    template_name = "heat_networks_library/pipe_create.html"
    success_url = reverse_lazy("heat_networks_library:index")
    context_object_name = "pipes"

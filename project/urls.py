from django.urls import path

from . import views
from .views import ProjectsListView, ProjectDetailView, ProjectEditView, ProjectDeleteView, ProjectCreateView

APP_NAME = 'project'

<<<<<<< HEAD
urlpatterns = (
    path('', views.index, name='index'),
    path('projects/', ProjectsListView.as_view(), name="projects"),
    path('project/<int:pk>', ProjectDetailView.as_view(), name="project_detail"),
    path('project/edit/<int:pk>', ProjectEditView.as_view(), name="project_edit"),
    path('project/<int:pk>/delete/', ProjectDeleteView.as_view(), name='project-delete'),
    path('project/create/', ProjectCreateView.as_view(), name='project-create')
)
=======
urlpatterns = [
    path('', views.index, name="projects"),

]
>>>>>>> 601ad97 (fix links for projects and home page)

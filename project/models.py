from django.db import models
from django.contrib.auth.models import User
from django.db.models import Q
# Create your models here.


class Projects(models.Model):
    project_name = models.CharField(max_length=50, unique=True)
    project_description = models.CharField(max_length=250, blank=True, null=True)
    users = models.ManyToManyField(User, related_name='users')
    created_on = models.DateTimeField(auto_now_add=True)
    created_by = models.ForeignKey(User, on_delete=models.CASCADE, related_name='project_author')
    updated_on = models.DateTimeField(auto_now=True)

    def user_has_access(self, user):
        return user == self.created_by or Projects.objects.filter(
            Q(created_by=user) | Q(users=user),
            pk=self.pk
        ).exists()

    def user_has_access_delete(self, user):
        return user == self.created_by
    def __str__(self):
        return self.project_name

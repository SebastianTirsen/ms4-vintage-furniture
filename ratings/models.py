from django.db import models
from django.contrib.auth.models import User


class Rating(models.Model):
    name = models.CharField(max_length=130)
    description = models.TextField(blank=True)
    user = models.ForeignKey(User, on_delete=models.DO_NOTHING, blank=True, null=True)

    def __str__(self):
        return self.name

from django.db import models
from django.conf import settings


class Rating(models.Model):
    name = models.CharField(max_length=130)
    description = models.TextField(blank=True)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.DO_NOTHING, blank=True, null=True)

    def __str__(self):
        return self.name


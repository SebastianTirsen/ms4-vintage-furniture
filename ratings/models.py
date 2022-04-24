from django.db import models


class Rating(models.Model):
    name = models.CharField(max_length=130)
    description = models.TextField(blank=True)

    def __str__(self):
        return self.name


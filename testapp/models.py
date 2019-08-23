from django.db import models

from django.contrib.postgres.fields import ArrayField
from django.db import models

class Post(models.Model):
    name = models.CharField(max_length=200)
    tags = ArrayField(models.CharField(max_length=200), blank=False)

    def __str__(self):
        return self.name

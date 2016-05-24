from __future__ import unicode_literals

from django.db import models

# Create your models here.
class CatalogueImages(models.Model):
    title = models.CharField(max_length = 20)
    images = models.FileField()

    def __unicode__(self):
        return self.title

from __future__ import unicode_literals

from django.db import models

# Create your models here.
class CatalogueImages(models.Model):
    title = models.CharField(max_length = 20)
    image = models.FileField()
    desc = models.CharField(max_length = 100, null=True, blank=True)

    def __unicode__(self):
        return self.title

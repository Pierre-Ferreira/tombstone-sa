from __future__ import unicode_literals

from django.db import models

# Create your models here.
class ContactUsInfo(models.Model):
    fullname = models.CharField(max_length = 120)
    emailAddr = models.EmailField()
    contactNo = models.CharField(max_length = 20)
    locationPersonal = models.CharField (max_length = 200)
    locationTombstone = models.CharField (max_length = 200)
    howManyTombstones = models.IntegerField()
    installationDate = models.CharField(max_length = 120)
    catalogueCodes = models.CharField(max_length = 120)
    colorTombstone = models.CharField(max_length = 120)
    otherInfo = models.TextField (max_length = 1000)
    timeStamp = models.DateTimeField(auto_now=False, auto_now_add=True)

    def __unicode__(self):
        return self.fullname

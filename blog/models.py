from django.db import models

# Create your models here.
class Entry(models.Model)
    name = models.CharField(max_length=30)

    def __unicode__(self):
        return self.name
    
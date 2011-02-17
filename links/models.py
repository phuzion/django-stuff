from django.db import models

# Create your models here.
class Link(models.Model):
	url = models.CharField(max_length=1024)
	name = models.CharField(max_length=255)
	def __unicode__(self):
		return self.name



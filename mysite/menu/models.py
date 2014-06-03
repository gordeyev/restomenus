from django.db import models
from mptt.models import MPTTModel, TreeForeignKey

class MenuRuUrls(models.Model):
	url = models.URLField(max_length=200)
	def __unicode__(self):
		return self.url

class NovikovUrls(models.Model):
	url = models.URLField(max_length=200)
	def __unicode__(self):
		return self.url

class AllResto(MPTTModel):
	name = models.CharField(max_length=200, unique=True)
	parent = TreeForeignKey('self', null=True, blank=True, related_name='children')

	class MTTMeta:
		order_insertion_by = ['name']

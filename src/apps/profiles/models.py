from __future__ import unicode_literals

from django.db import models

class profile(models.Model):
	name = models.Charfield(max_length=200)
	def __unicode__(self):
		return self.name
		
from __future__ import unicode_literals
from django.db import models


class Table(models.Model):
	name=models.CharField(max_length=30)
	admn_no=models.IntegerField()
	password=models.CharField(max_length=30)
	branch=models.CharField(max_length=30)
	year=models.DateField()
	access=models.IntegerField(default=0000.000)
	def __unicode__(self):
		return self.name


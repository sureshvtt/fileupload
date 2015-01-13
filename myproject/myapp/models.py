# -*- coding: utf-8 -*-
from django.db import models
import datetime

def file(self, filename):
	ext = filename.split('.')[1]
	if ext == 'swf':
		url = "uploads/%s/%s/%s/%s/%s/%s" % (self.domain, 'swf', datetime.datetime.today().year, datetime.datetime.today().month, datetime.datetime.today().day , filename)
	else:
		url = "uploads/%s/%s/%s/%s/%s/%s" % (self.domain, 'image', datetime.datetime.today().year, datetime.datetime.today().month, datetime.datetime.today().day , filename)
	return url

class Document(models.Model):
	domain = models.CharField(max_length=1024)
	docfile = models.FileField(upload_to=file)

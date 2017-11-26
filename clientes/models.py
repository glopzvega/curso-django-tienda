# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.

class Cliente(models.Model):
	nombre = models.CharField(max_length=255)
	apellidop = models.CharField(max_length=255)
	apellidom = models.CharField(max_length=255)
	email = models.EmailField(max_length=255)

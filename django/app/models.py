# -*- encoding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

from django.contrib.auth.models import User

class Estudiantes(models.Model):
	nombre = models.TextField()
	apellido = models.TextField()
	administrador = models.ForeignKey(User)

	class Meta:
		verbose_name = "Estudiante"
		verbose_name_plural = "Estudiantes"

	def __unicode__(self):
		return self.nombre
from django.contrib import admin

from .models import Estudiantes

@admin.register(Estudiantes)
class EstudiantesAdmin(admin.ModelAdmin):
	pass
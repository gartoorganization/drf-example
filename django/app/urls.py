# -*- encoding: utf-8 -*-
from django.conf.urls import url, include
from .views import(
	LoginView, EstudiantesView
	)
urlpatterns = [
	url(r'^ingreso/$', LoginView.as_view(), name="api-login"),
	url(r'^estudiantes/$', EstudiantesView.as_view(), name="api-students"),
	url(r'^estudiantes/(?P<pk>[0-9]+)/$', EstudiantesView.as_view(), name="api-students-detail"),
]
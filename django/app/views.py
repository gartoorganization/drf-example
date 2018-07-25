# -*- encoding: utf-8 -*-

from django.shortcuts import render

from rest_framework import parsers, renderers, generics, status, mixins

from rest_framework.authentication import SessionAuthentication, BasicAuthentication, TokenAuthentication

from rest_framework.authtoken.models import Token

from rest_framework.authtoken.serializers import AuthTokenSerializer

from rest_framework.permissions import AllowAny, IsAuthenticated

from rest_framework.renderers import JSONRenderer

from rest_framework.response import Response

from rest_framework.views import APIView

from .serializers import (
		EstudiantesSerializer
	)

from .models import Estudiantes

class LoginView(APIView):
	"""
	esta clase es para el login
	"""
	throttle_classes = ()
	permission_classes = ()
	parser_classes = (parsers.FormParser, parsers.MultiPartParser, parsers.JSONParser,)
	renderer_classes = (renderers.JSONRenderer,)
	serializer_class = AuthTokenSerializer

	def post(self, request):
		serializer = self.serializer_class(data=request.data)
		serializer.is_valid(raise_exception=True)
		user = serializer.validated_data['user']
		token, created = Token.objects.get_or_create(user=user)
		return Response({'token': token.key})

class EstudiantesView(generics.ListCreateAPIView, mixins.UpdateModelMixin, mixins.DestroyModelMixin):
	"""
		Clase para el manejo de estudiantes
	"""
	authentication_classes = (SessionAuthentication, BasicAuthentication, TokenAuthentication)
	permission_classes = (IsAuthenticated,)
	serializer_class = EstudiantesSerializer

	def get_queryset(self):
		return Estudiantes.objects.filter(administrador=self.request.user)

	def post(self, request, *args, **kwargs):
		request.data['administrador'] = request.user.id
		return super(EstudiantesView, self).post(request, *args, **kwargs)

	def put(self, request, *args, **kwargs):
		return self.update(request, *args, **kwargs)

	def delete(self, request, *args, **kwargs):
		return self.destroy(request, *args, **kwargs)
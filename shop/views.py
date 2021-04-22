from django.shortcuts import render
from django.contrib.auth.models import User
# Create your views here.
from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view

from .serializers import  RegistrationSerializer 

from django.conf import settings
from django.db.models.signals import post_save
from django.dispatch import receiver
from rest_framework.authtoken.models import Token
from django.http import HttpResponse


def index(request):
    return HttpResponse('API')

@api_view(['POST'])
def signup(request):
    if request.method == 'POST':
        serializer = RegistrationSerializer(data = request.data)
        data = {}
        if serializer.is_valid():
            user = serializer.save()
            data['response'] = 'User Created successfully'
            data['email'] = user.email
            data['username'] = user.username
            token = Token.objects.get(user=user).key
            data['token'] = token
        else:
            data = serializer.errors
        return Response(data)


@receiver(post_save,sender = settings.AUTH_USER_MODEL)
def create_auth_token(sender,instance= None,created = False,**kwargs):
    if created:
        Token.objects.create(user=instance)



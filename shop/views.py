from django.shortcuts import render
# Create your views here.
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .serializers import  RegistrationSerializer ,ProductSerializer
from django.conf import settings
from django.db.models.signals import post_save
from django.dispatch import receiver
from rest_framework.authtoken.models import Token
from rest_framework.views import APIView
from .models import Product




def index(request):
    login = 'csx.pythonanywhere.com/login/'
    signup = 'csx.pythonanywhere.com/signup/'
    params = {'login': login,'signup': signup }
    return render(request,'shop/index.html',params)


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



class ProductView(APIView):
    def get(self, request):
        data = request.data
        
        
        
        if 'id' in data.keys():
            product = Product.objects.get(id = id)
            serializer = ProductSerializer(product)
            return Response(serializer.data)
        
        products = Product.objects.all()
        serializer = ProductSerializer(products,many = True)
        return Response(serializer.data)
    
    
    def post(self, request):
        serializer = ProductSerializer(data = request.data)
        data = {}
        if serializer.is_valid():
            product = serializer.save()
            data  = serializer.data
            data['response'] = 'Product added successfully'
        else:
            data = serializer.errors
        return Response(data)



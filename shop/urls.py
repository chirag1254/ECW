from django.urls import path
from . import views
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.authtoken.models import Token
from rest_framework.response import Response

class CustomAuthToken(ObtainAuthToken):

    def post(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data,
                                           context={'request': request})
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data['user']
        token, created = Token.objects.get_or_create(user=user)
        return Response({
            'token': token.key,
            'username': user.username,
            'email': user.email
        })

urlpatterns = [
    path('signup/',views.signup,name = 'signup'),
    path('login/',CustomAuthToken.as_view(),name = 'login'),
    path('',views.index, name = 'index'),
    path('product/<int:id>', views.ProductView.as_view(),name = 'product'),



]
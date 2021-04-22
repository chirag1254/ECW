from django.urls import path
from . import views
from rest_framework.authtoken.views import obtain_auth_token

urlpatterns = [
    path('',views.index,name = 'index'),
    path('signup/',views.signup,name = 'signup'),
    path('login/',obtain_auth_token,name = 'login'),


]
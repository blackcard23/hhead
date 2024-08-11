from django.urls import path, include

from main.views import SpisokVakansii
from accounts.views import *

urlpatterns = [
    path('', UserLoginView.as_view(), name='login'),
    path('register/', UserRegisterView.as_view(), name='register'),
    path('logout/', user_logout, name='logout'),
    path('main/', SpisokVakansii.as_view(), name='main'),
    path('', include('main.urls')),
]

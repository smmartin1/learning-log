'''Defines URL patterns for accounts.'''

from django.urls import path, include
from . import views

app_name = 'accounts'
urlpatterns = [
    path('', include('django.contrib.auth.urls')),          #Default auth url
    path('register/', views.register, name = 'register')    #Registration page
]
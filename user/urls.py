from django.urls import path
from .import views

urlpatterns = [
    path('index/', views.index),
    path('', views.index),
    path('about/', views.about),
    path('contact/', views.contact),
    path('login/', views.login),
    path('signin/', views.signin),
    path('batches/', views.mynewbatches),
    path('facility/', views.facility),
    path('stories/', views.stories),
    path('feedback/', views.feedback),
]
from django.urls import path
from . import views

urlpatterns = [
    path('', views.user_form, name='user_form'),  
    path('user_form/', views.user_form, name='user_form'),

]

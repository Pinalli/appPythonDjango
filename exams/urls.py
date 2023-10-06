from django.urls import path
from . import views

urlpatterns = [
    path('request_exams/', views.request_exams, name='request_exams'),  
  ]

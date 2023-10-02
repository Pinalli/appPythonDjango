from django.urls import path
from . import views


urlpatterns = [
    path('cadastre/', views.cadastre, name='cadastre'),    
]
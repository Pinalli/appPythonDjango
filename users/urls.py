from django.urls import path
from users import views

urlpatterns = [
    path('cadastre/', views.cadastre, name='cadastre'),    
]
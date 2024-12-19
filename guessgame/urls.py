from django.urls import path
from . import views

urlpatterns = [
    path('resultt/', views.resultt, name="resultt"),
    path('',views.guess,name="index"),
    
]
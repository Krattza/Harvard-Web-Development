from django.urls import path
from . import views

app_name = "calculator"
urlpatterns = [
    path('', views.calculations, name='calcualtions'),
    path('result/', views.result, name='result'),
]
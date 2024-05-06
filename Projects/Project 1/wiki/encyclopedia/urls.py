from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("<str:title>", views.titles, name='title'),
    path('entryPage', views.createEntries, name='entryPage')
]

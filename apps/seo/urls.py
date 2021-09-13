from django.contrib import admin
from django.urls import path, include
from . import views


urlpatterns = [
    path('position/<int:type>/<str:keyword>', views.get_pos),
]

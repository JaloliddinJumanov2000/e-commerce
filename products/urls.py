from django.contrib import admin
from django.urls import path, include
from djoser.urls.base import router

urlpatterns = [
    path('', include(router.urls)),
    ]
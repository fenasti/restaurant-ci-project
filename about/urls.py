from . import views
from django.urls import path

urlpatterns = [
    path('', views.about_info, name='about'),
]
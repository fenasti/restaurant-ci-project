from . import views
from django.urls import path

urlpatterns = [
    path('', views.reservation_page, name='reservation'),
]
from . import views
from django.urls import path

urlpatterns = [
    path('', views.reservation_page, name='reservation'),
    path('edit_reservation/<int:reservation_id>', views.reservation_edit, name='reservation_edit'),
]
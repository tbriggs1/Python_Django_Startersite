from django.urls import path

from . import views

urlpatterns = [
    path('<int:id>', views.detail, name="detail"),
    path('room', views.rDetail, name="room"),
    path('new', views.new, name="new"),
]
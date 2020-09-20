from django.urls import path
from . import views

urlpatterns = [
    path("", views.home, name="HomePage"),
    path("detail/<int:id>",  views.detail, name="detail"),
]


from django.urls import path
from . import views

urlpatterns = [
    #    path("", views.home, name="HomePage"),
    path("", views.HomeView.as_view(), name="home"),
    #    path("detail/<int:id>",  views.detail, name="detail"),
    path("detail/<int:pk>",  views.ContactDetailView.as_view(), name="detail"),
    path('search/', views.search, name="search"),
    path('contacts/create', views.ContactCreateView.as_view(), name="create"),
]

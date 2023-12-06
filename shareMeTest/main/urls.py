from django.urls import path
from main import views

urlpatterns = [
    path("", views.homePage, name="homePage"),
    path("options/", views.options, name="options"),
    path("optionCreation/", views.optionCreation, name="optionCreation"),
]


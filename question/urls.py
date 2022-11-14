from django.urls import path

from .views import Questions

urlpatterns = [
    path("all", Questions.as_view())
]

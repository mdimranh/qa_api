from django.urls import path

from .views import *

urlpatterns = [
    path("registration", Registration.as_view()),
    path("<int:id>", UserDetails.as_view()),
    path("all", Users.as_view()),
]

from django.urls import path
from rest_framework_simplejwt.views import (TokenBlacklistView,
                                            TokenObtainPairView,
                                            TokenRefreshView)

from .views import *

urlpatterns = [
    path("registration", Registration.as_view()),
    path("token", TokenObtainPairView.as_view()),
    path("token/refresh", TokenRefreshView.as_view()),
    path('logout', TokenBlacklistView.as_view(), name='token_blacklist'),
    path("<int:id>", UserDetails.as_view()),
    path("sheikh/all", Sheikhs.as_view()),
]

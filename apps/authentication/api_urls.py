from django.urls import path
from rest_framework_simplejwt.views import (TokenObtainPairView, TokenRefreshView,)
from .views import CurrentUserAPIView, RegisterUserAPIView

app_name = 'apps.authentication'

urlpatterns = [
    path('login/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('login/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('current-user/', CurrentUserAPIView.as_view()),
    path('register/', RegisterUserAPIView.as_view())
]

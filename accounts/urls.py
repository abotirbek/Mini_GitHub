from django.urls import path
from .views import RegisterAPIView, ChangePasswordView
from rest_framework_simplejwt.views import TokenObtainPairView


urlpatterns = [
    path('register/', RegisterAPIView.as_view()),
    path('login/', TokenObtainPairView.as_view(), name='login'),
    path('change-password/', ChangePasswordView.as_view(), name='change-password')
]
from django.urls import path
from .views import register, login, verify_email

urlpatterns = [
    path('register/', register, name='register'),
    path('login/', login, name='login'),
    path("verify/<uidb64>/<token>/", verify_email, name="verify-email"),
]

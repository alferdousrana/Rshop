from django.urls import path
from .views import register, user_login, verify_email, profile, logout_view

urlpatterns = [
    path('register/', register, name='register'),
    path('login/', user_login, name='login'),
    path("verify/<uidb64>/<token>/", verify_email, name="verify-email"),
    path("profile/", profile, name="profile"),
    path("logout/", logout_view, name="logout"),
]

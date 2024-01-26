from django.urls import path
from accounts.views import signup, user_login, user_logout

urlpatterns = [
    path("logout/", user_logout, name = "user_logout"),
    path("signup/", signup, name="signup"),
    path("login/", user_login, name = "user_login"),
]
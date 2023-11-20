from django.contrib.auth.views import LoginView, LogoutView
from users.apps import UsersConfig
from django.urls import path
from users.views import RegisterView, VerificationView, ErrorVerification

app_name = UsersConfig.name

urlpatterns = [
    path('', LoginView.as_view(template_name='users/login.html'), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('register/', RegisterView.as_view(), name='register'),
    path('verification/', VerificationView.as_view(), name='verification'),
    path('verify_email/error/', ErrorVerification.as_view(), name='verify_email_error'),
]
from django.urls import path
from .views import signup, dashboard, password_change_form, register

urlpatterns = [
    path('signup/', signup, name = 'signup'),
    path('register/', register, name = 'register'),
    # path('signup/', SignUpView.as_view(), name='signup'),
    path('', dashboard, name = 'dashboard'),
    path('password_change/', password_change_form, name = 'password_change')
]
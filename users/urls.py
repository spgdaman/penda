from django.urls import path
from .views import signup, dashboard, password_change_form

urlpatterns = [
    path('signup/', signup, name = 'signup'),
    path('dashboard/', dashboard, name = 'dashboard'),
    # path('password_change/', password_change_form, name = 'password_change')
]
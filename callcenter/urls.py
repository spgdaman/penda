from django.urls import path
from .views import calllogs, call_volumes #form_test

urlpatterns = [
    path('3cx/',calllogs, name = 'call_logs'), 
    # path('form_test/',form_test),
    path('call_volumes/', call_volumes, name = 'call_volumes'),
]

from django.forms import ModelForm
from django import forms
from .models import CallLogs

class FormTest(ModelForm):
    class Meta:
        model = CallLogs
        fields = '__all__'

class UploadCallVolumesForm(forms.Form):
    file = forms.FileField()
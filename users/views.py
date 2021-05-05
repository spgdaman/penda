from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login, authenticate
from django.contrib import messages

from django.urls import reverse_lazy
from django.views import generic
from .forms import SignUpForm

# def signup(request):
#     if request.method == 'POST':
#         form = SignUpForm(request.POST)
#         if form.is_valid():
#             user = form.save()
#             user.refresh_from_db() # load the profile instance created by the signal
#             user.profile.birth_date = form.cleaned_data.get('birth_date')
#             user.save()
#             raw_password = form.cleaned_data.get('password1')
#             user = authenticate(username=user.username, password = raw_password)
#             login(request,user)
#             return redirect('dashboard')
#     else:
#         form = SignUpForm()
#     return render(request, 'registration/signup.html', {'form': form})

# class SignUpView(generic.CreateView):
#     form_class = UserCreationForm
#     success_url = reverse_lazy('login')
#     template_name = 'registration/signup.html'

def signup(request):
    if request.method == "POST":
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            username = form.cleaned_data.get('username')
            messages.success(request, f'Account created for {username}')
            return redirect('dashboard')
        messages.error(request, "Unsuccessful registration. Invalid information.")
    else:
        form = SignUpForm()
        return render(request, 'registration/signup.html', {'form': form})

def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            print(form)
        return redirect('dashboard')
    else:
        form = UserCreationForm()
    return render(request, 'registration/signup.html', {"form":form})


def dashboard(request):
    return render(request,'registration/dashboard.html')

def password_change_form(request):
    return render(request, 'registration/password_change_form')
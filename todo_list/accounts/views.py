from .forms import RegisterForm
from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import login, logout
# Create your views here.

def register_view(request):
    if request.method == 'GET':
        form = RegisterForm()
        return render(request, 'html/register.html', {'form':form})

    
    if request.method == 'POST':
        form = RegisterForm(request.POST) 
        if form.is_valid():
            user = form.save(commit=False)
            user.username = user.username.lower()
            user.save()
            messages.success(request, 'Singed up successfully.')
            login(request, user)
            return redirect('/home')
        else:
            return render(request, 'html/register.html', {'form': form})

def sign_in_view(request):
    ...


def sign_out_view(request):
    ...


def sign_up_view(request):
    ...


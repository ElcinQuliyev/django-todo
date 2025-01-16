from .forms import RegisterForm
from django.contrib.auth.forms import AuthenticationForm
from django.shortcuts import render, redirect
from django.contrib.auth import login, logout

def register_view(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.username = user.username.lower()
            user.save()
            login(request, user)
            return redirect('/todo_list')  # Redirect after successful registration
        else:
            return render(request, 'html/register.html', {'form': form})
    else:
        form = RegisterForm()
        return render(request, 'html/register.html', {'form': form})

def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            if 'next' in request.POST:
                next_page = request.POST.get('next', '/home')  
                return redirect(next_page)
            else:
                return redirect('/todo_list')
        else:
            return render(request, 'html/login.html', {'form': form})
    else:
        form = AuthenticationForm()
        return render(request, 'html/login.html', {'form': form})

def logout_view(request):
    if request.method == "POST":
        logout(request)
        return redirect('/login')
    return redirect('/home')    
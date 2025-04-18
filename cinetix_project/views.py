from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from .forms import LoginForm


@login_required(login_url='login')
def test_page(request):
    context = {
        'test': 'test',
    }
    return render(request, 'test.html', context)


def login_page(request):
    forms = LoginForm()
    if request.method == 'POST':
        forms = LoginForm(request.POST)
        if forms.is_valid():
            username = forms.cleaned_data['username']
            password = forms.cleaned_data['password']
            user = authenticate(username=username, password=password)
            if user:
                login(request, user)
                return redirect('cinetix:film-list')
    context = {
        'form': forms
    }
    return render(request, 'login.html', context)
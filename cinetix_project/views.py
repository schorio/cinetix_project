from django.shortcuts import render, redirect
from django.contrib import messages 
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import AuthenticationForm

def login_page(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        
        ut = authenticate(request, username=username, password=password)
        
        if ut is not None:
            login(request, ut)
            return redirect("mangalib:index")
        else:
            messages.info(request, "Misy diso")
            
    form = AuthenticationForm()
    return render(request, "login.html", {'form': form})
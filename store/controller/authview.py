from django.contrib.auth import *
from django.shortcuts import redirect, render
from django.contrib import messages

from store.forms import CusomUserForm


def register(request):
    form = CusomUserForm()
    if request.method == 'POST':
        form = CusomUserForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Registered Successfully! Login to Continue")
            return redirect('/login')
    context = {'form':form}
    return render(request, "store/auth/register.html", context)


def loginpage(request):
    if request.user.is_authenticated:
        messages.success(request, "You are alrady logged in")
        return redirect('/')
    else:
        if request.method == 'POST':
            name = request.POST.get('username')
            passwd = request.POST.get('password')
            
            user = authenticate(request, username=name, password = passwd )
        
            if user is not None:
                login(request, user)
                messages.success(request, "Logged in Successfully")
                return redirect("/")
            else:
                messages.error(request, "Invalid Username or Password")
                return redirect("/login")
                
            
    
        return render(request, "store/auth/login.html")
    
def logoutpage(request):
    if request.user.is_authenticated:
        logout(request)
        messages.success(request, "Logged out Successfully")
    return redirect("/")
    
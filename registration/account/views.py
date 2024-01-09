from django.shortcuts import render, redirect
from .forms import signupform, loginform
from django.contrib.auth import authenticate, login
# Create your views here.

def lognsign(request):
    return render (request, 'lognsign.html')

def signuppage(request):
    nsg = None
    if request.method == 'POST':
        forms = signupform(request.POST)
        if forms.is_valid():
            user = forms.save()
            return redirect('login.html')
        else:
            nsg = 'form is not valid'
    else:
        forms = signuppage,
        return render(request, 'signup.html')

def loginpage(request):
    forms = loginform(request.POST or None)
    nsg = None
    if request.method == 'POST':
        if forms.is_valid():
            username = forms.cleaned_data.get(username)
            Password = forms.cleaned_data.get(Password)
            user = authenticate(username=username, Password=Password)
            if user is not None:
                login(request, user)
                return redirect('home')
            else:
                nsg = 'inavlid credentials'
        else:
            nsg = "error validating forms"
    return render(request, 'login.html', {'form':forms, 'nsg':nsg})

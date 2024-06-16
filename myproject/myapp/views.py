from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.decorators import login_required
from .forms import AddBillForm ,CustomAuthenticationForm,CustomUserCreationForm
from django.contrib import messages
def signup(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('home')  # Redirect to a homepage or another page after signup
    else:
        form = CustomUserCreationForm()
    return render(request, 'signup.html', {'form': form})

def login_view(request):
    if request.method == 'POST':
        form = CustomAuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('home')  # Redirect to a homepage or another page after login
    else:
        form = CustomAuthenticationForm()
    return render(request, 'login.html', {'form': form})
@login_required
def home(request):
    return render(request, 'home.html')

@login_required
def logout_view(request):
    logout(request)
    return redirect('login')  # Redirect to the login page after logout

def addBills(request):
    if request.method== "POST":
        form = AddBillForm(request.POST,request.FILES)
        if form.is_valid():
            bill=form.save(commit=False)
            bill.user=request.user
            bill.save()
            messages.success(request, "Your bill has been successfully submitted!")
            return redirect('addBills')
    else:
        form = AddBillForm()
    return render(request,"add_bill.html" ,{'form':form})
    
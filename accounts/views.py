# accounts views
from django.core.exceptions import PermissionDenied
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required, user_passes_test
from django.shortcuts import redirect, render
from .forms import UserForm
from vendor.forms import VendorForm
from .models import User, UserProfile

from .utils import detect_user # TODO add into docs

# restrict the vendor accesing from cut dashboard
def check_role_vendor(user):
    if user.role == 1:
        return True
    else:
        raise PermissionDenied

# restrict the cust accesing from vendor dashboard
def check_role_cust(user):
    if user.role == 2:
        return True
    else:
        raise PermissionDenied

# Create your views here.
def registerUser(request):
    if request.user.is_authenticated:
        messages.warning(request, 'You are an registerd user already')
        return redirect('dashboard')
    elif request.method == 'POST':
        form = UserForm(request.POST)
        if form.is_valid():
            #1 way: create user by form
            # password = form.cleaned_data['password']
            # user =  form.save(commit=False)
            # user.set_password(password)
            # user.role = User.CUSTOMER
            # user.save()
            
            #2 way: to create using create_user()
            first_name = form.cleaned_data['first_name']
            last_name = form.cleaned_data['last_name']
            username = form.cleaned_data['username']
            email = form.cleaned_data['email']
            password = form.cleaned_data['password']
            user = User.objects.create_user(
                first_name=first_name, 
                last_name=last_name,
                username=username,
                email=email,
                password=password
                )
            user.role = User.CUSTOMER
            user.save()
            messages.success(request, 'you account is created successfully')
            
            return redirect('registerUser')
        else:
            messages.warning(request, 'invalid form data')
    else:    
        form = UserForm()
    context = {'form':form}
    return render(request, 'accounts/registerUser.html',context)

def registerVendor(request):
    
    if request.method == 'POST':
        form = UserForm(request.POST)
        v_form = VendorForm(request.POST, request.FILES)
        if form.is_valid() and v_form.is_valid():
            # grabing he data from the user form and creating a account and as well as resuartant account 
            first_name = form.cleaned_data['first_name']
            last_name = form.cleaned_data['last_name']
            username = form.cleaned_data['username']
            email = form.cleaned_data['email']
            password = form.cleaned_data['password']
            user = User.objects.create_user(
                first_name=first_name, 
                last_name=last_name,
                username=username,
                email=email,
                password=password
                )
            user.role = user.VENDOR
            user.save()
            # grab vendor form data and store
            vendor  = v_form.save(commit=False)
            vendor.user = user
            user_profile = UserProfile.objects.get(user=user)
            vendor.user_profile = user_profile
            vendor.save()
            
            messages.success(request, "Your account has been registered and wait for the approval.")
            return redirect('login')
        else:
            messages.warning(request, 'Invalid form data')
        
    else:
        form = UserForm()
        v_form = VendorForm()
    context = {'form':form, 'v_form':v_form }
    return render(request, 'accounts/registerVendor.html' ,context)


def handle_login(request):
    if request.user.is_authenticated:
        messages.warning(request, 'You are already logged in')
        return redirect('dashboard')
    if request.method == 'POST':
        user_email = request.POST.get('email')
        user_password = request.POST.get('password')
        
        user = authenticate(email=user_email, password = user_password)
        if user is not None:
            login(request, user)
            messages.success(request, 'You have successfully logged in')
            return redirect('myAccount')
        else:
            messages.warning(request, 'Invalid Email or password')
            return redirect('login')
    return render(request, 'accounts/login.html')


def handle_logout(request):
    logout(request)
    messages.info(request, 'you have been logged out')
    return redirect('login')
    return render(request, 'accounts/logout.html') 

@login_required(login_url = 'login')
def myAccount(request):
    user = request.user
    redirectUrl = detect_user(user)
    return redirect(redirectUrl)

@login_required(login_url = 'login')
@user_passes_test(check_role_cust)
def custDashboard(request):
    context = {}
    return render(request, 'accounts/custDashboard.html', context)

@login_required(login_url = 'login')
@user_passes_test(check_role_vendor)
def vendorDashboard(request):
    context = {}
    return render(request, 'accounts/vendorDashboard.html', context)
# accounts views
from django.contrib import messages
from django.shortcuts import redirect, render
from .forms import UserForm
from vendor.forms import VendorForm
from .models import User, UserProfile




# Create your views here.
def registerUser(request):
    if request.method == 'POST':
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
            return redirect('registerVendor')
        else:
            messages.warning(request, 'Invalid form data')
        
    else:
        form = UserForm()
        v_form = VendorForm()
    context = {'form':form, 'v_form':v_form }
    return render(request, 'accounts/registerVendor.html' ,context)
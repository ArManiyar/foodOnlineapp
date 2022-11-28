# accounts views
from django.contrib import messages
from django.shortcuts import redirect, render
from .forms import UserForm
from .models import User
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
            messages.error(request, 'Something went wrong')
    else:    
        form = UserForm(request.POST)
    context = {'form':form}
    return render(request, 'accounts/registerUser.html',context)
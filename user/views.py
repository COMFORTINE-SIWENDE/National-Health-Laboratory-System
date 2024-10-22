from django.shortcuts import render,redirect
from django.contrib.auth.views import LoginView
from .forms import *
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import AuthenticationForm
from .forms import UpdateUserForm, ProfileUpdateForm
# Create your views here.
# registration
# @login_required
def sign_up(request):
    if request.method == 'POST':
        form = CreateUserForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = CreateUserForm()
    context = {"form":form}
    return render(request, 'authentication/sign_up.html',context)

# login
def Custom_login(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('admin_panel')
    else:
        form = AuthenticationForm()
    return render(request, 'authentication/login.html', {'form': form})
@login_required
def profile(request):
    context = {}
    return render(request, 'partials/profile.html',context)
def profile_update(request):
    if request.method == 'POST':
        user_form = UpdateUserForm(request.POST, instance=request.user)
        profile_form = ProfileUpdateForm(request.POST,request.FILES, instance=request.user.profile)
        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            profile_form.save()
            return redirect('profile')
    else:
        user_form = UpdateUserForm(instance=request.user)
        profile_form = ProfileUpdateForm(instance=request.user.profile)

    context = {
        'user_form':user_form,
        'profile_form':profile_form
    }
    return render(request, 'partials/profile_update.html', context)
@login_required
def users(request):
    users = User.objects.all()
    context = {
        'users':users
    }
    return render(request, 'dashboard/adm_users.html', context)
def staff_detail(request, pk):
    staff = User.objects.get(id=pk)
    context = {
        'staff':staff

    }
    return render(request,'dashboard/staff_detail.html',context )
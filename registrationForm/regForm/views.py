from django.shortcuts import render,redirect
from regForm.forms import UserForm,UserProfileForm
from django.contrib.auth import authenticate,login,logout
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
# Create your views here.


def registration(request):
    registered = False
    if request.method == 'POST':
        form = UserForm(request.POST)
        form1 = UserProfileForm(request.POST,request.FILES)
        if form.is_valid() and form1.is_valid():
            user = form.save()
            user.set_password(user.password)
            user.save()

            profile = form1.save(commit=False)
            profile.user = user
            profile.save()
            registered = True
    else:
        form = UserForm()
        form1 = UserProfileForm()
    
    context = {
        "form" : form,
        'form1':form1,
        'registered' : registered
    }

    return render(request,"registration.html",context)


def user_login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        print(username)
        print(password)
        user = authenticate(username=username,password=password)

        if user:
            if user.is_active:
                login(request,user)
                return redirect('home')
        else:
            return HttpResponse("Please check your creds..!")
    return render(request,'login.html',{})


@login_required(login_url='login')
def home(request):
    return render(request,'home.html',{})

@login_required(login_url='login')
def profile(request):
    return render(request,'profile.html',{})

def user_logout(request):
    logout(request)
    return redirect('login')
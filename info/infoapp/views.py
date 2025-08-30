from django.shortcuts import render,redirect
from .forms import UserForm, userDetails

# Create your views here.
def index(request):
    my_form = UserForm()
    if request.method == "POST":
        form = UserForm(request.POST,request.FILES)
        if form.is_valid():
            print("succss")
            form.save()
            return redirect('display')
    return render(request,'index.html',{'form':my_form})

def display(request):
    var = userDetails.objects.all()
    print(var)
    return render(request,'display.html',{'var':var})

def profile(request):
    data = userDetails.objects.filter(id=2)
    return render(request,"profile.html",{'var':data})

def contact(request):
    return render(request,"contact.html")

def about(request):
    return render(request,"about.html")


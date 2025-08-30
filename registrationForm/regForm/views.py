from django.shortcuts import render
from regForm.forms import UserForm,UserProfileForm
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

    # form = UserForm()
    # form1= UserProfileForm()
    # context = {
    #     "form" : form,
    #     'form1':form1
    # }
    # if request.method == "POST":
    #     form = UserForm(request.POST)
    #     form1 = UserProfileForm(request.POST)
    #     if form.is_valid() and form1.is_valid() :
    #         print("validation Scuccess")
    #         form.save()# work only u have created the model forms 
    #         print(form.cleaned_data["username"], form1.cleaned_data["phone"])
    return render(request,"registration.html",context)


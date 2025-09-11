from django.shortcuts import render
from carsapp.models import Company,Products
from django.contrib.auth.decorators import login_required

# Create your views here.
@login_required(login_url='login')
def showProduct(request):
    comp_names = Company.objects.all()
    return render(request,'cars/products.html',{'comp_name':comp_names})

@login_required(login_url='login')
def company_details(request,id=0):
    company = Company.objects.get(id=id)
    print(company)
    return render(request,'cars/compDetails.html',{'company':company})

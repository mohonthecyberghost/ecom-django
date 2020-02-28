import datetime

from django.contrib.auth import authenticate
from django.contrib.auth.decorators import login_required, user_passes_test
from django.contrib.auth.models import User, Group
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth import login as auth_login, logout as auth_logout, authenticate

# Create your views here.
from registration.models import CompanyRegistration


def index(request):
    return render(request, 'registration/seller_registraion.html')


def companyRegistration(request):
    if request.method == 'POST':
        companyName = request.POST.get('companyName')
        PersonName = request.POST.get('PersonName')
        contractNumber = request.POST.get('contractNumber')
        image = request.FILES.get('image')

        bankAccount = request.POST.get('bankAccount')
        address = request.POST.get('address')
        emailAddress = request.POST.get('emailAddress')
        password = request.POST.get('password')

        user = create_user(companyName, emailAddress, password)
        company = CompanyRegistration(PersonName=PersonName, contractNumber=contractNumber, emailAddress=emailAddress,
                                      companyName=companyName,
                                      password=password, image=image, bankAccount=bankAccount, address=address,
                                      user=user)
        company.save()

        return HttpResponse("test")


# @login_required()
def companyLogin(request):
    context = dict()
    context['msg'] = "successfully Registered"
    return render(request, 'registration/seller_login.html', context)


def login(request):
    if request.method == "POST":
        username = request.POST['userName']
        password = request.POST['password']
        auth = authenticate(request, username=username, password=password)
        usr = User.objects.get(username=username)

        rate = User.objects.filter(pk=usr.id, groups__name='company').exists()
        if rate and auth is not None:
            auth_login(request, auth)
            return redirect('eshopadmin:index')
        else:
            return HttpResponse("failed" + "" + str(usr.id))


def create_user(username, email, password):
    user = User(username=username,
                is_superuser=False,
                is_active=True,
                is_staff=False,
                email=email,
                date_joined=datetime.datetime.now())
    user.save()
    user.set_password(password)

    group = Group.objects.get(name='company')

    user.groups.add(group)
    user.save()
    return user

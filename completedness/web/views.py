# from http.client import HTTPResponse
# from re import template
import re
from urllib import response
from django.shortcuts import render, redirect
from .login import NewUserForm
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.forms import AuthenticationForm
from django.contrib import messages
from django.http import HttpResponse, HttpResponseRedirect
from bs4 import BeautifulSoup
from db import models

def register(request):
    if request.method == "POST":
        form = NewUserForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request, "Registration successful.")

            # post data to user db
            username = request.POST.get('username')
            password = request.POST.get('password2')
            dbData = models.users(name=username,password=password,points=0)
            # dbData.save()

            # redirect to success page
            HttpResponse.set_cookie('username', username)
            return redirect("web:success")
        messages.error(request, "Unsuccessful registration. Invalid information.")
    form = NewUserForm()
    return render (request=request, template_name="web/register.html", context={"register_form": form})

def userLogin(request):
    if request.method=='POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                # response = HttpResponseRedirect()
                # response.url('web:authLogon')
                # print (response)
                # HttpResponse.set_cookie('username',username)
                login(request, user)
                messages.info(request, f'You are now logged in as {username}.')
                return redirect('web:authLogon')
                # return response
            else:
                messages.error(request,'Invalid username or password')
        else:
            messages.error(request,'Invalid username or password')
    form = AuthenticationForm()
    return render(request=request, template_name='web/login.html', context={'login_form':form})

def userLogout(request):
    logout(request)
    messages.info(request, 'You have log out successfully.')
    return redirect('web:login')

# views from web
def index(request):
    return render(request, 'index.html')
    # return HttpResponse("test")

def success(request):
     return render(request, 'web/success.html')

# views after logon
def logonIndex(request):
    return render(request, 'logon/authIndex.html')

def getSomeUsersPoints(request):
    if request.method == "GET":
        data = models.users.objects
        return


def getSeminar(request):
    print(request)
    if request.method == "GET":
        data = models.workshops.objects.all()
        # for rows in data:
        #     print(rows.name)

    return render(request, 'logon/seminar.html', {'data': data})

def postSeminar(request):
    print(request.COOKIES)
    # getSomeUsersPoints(request)
    # add points
    points = 5

    
    # to return back to seminar page
    data = models.workshops.objects.all()
    return render(request, 'logon/seminar.html', {'data': data})

def getActivity(request):
    if request.method == "GET":
        data = models.eca.objects.all()
    return render(request, 'logon/activity.html', {'data': data})

def postActivity(request):
    return

def getConnections(request):
    if request.method == "GET":
        data = models.connections.objects.all()
    return render(request, 'logon/connections.html', {'data': data})

from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from .models import tbl_Authentication
from django.http import HttpResponse
from django.db import connection
from django.template import loader
from .models import Status




# Create your views here.

def base(request):
    return render(request, 'base.html')


def user_login(request):
    print(request)
    if request.method == 'POST':
        print("ca post")
        username = request.POST.get('username')
        password = request.POST.get('password')

        try:
            user = authenticate(username=username, password=password)
            print(user)
            if user is not None:
                return render(request, 'dashboard.html', {})
            else:
                return HttpResponse("Invalid Password!")
                print("Someone tried to login and failed.")
                print("They used username: {} and password: {}".format(username, password))

                return redirect('/')
        except Exception:
            return redirect('/')

    else:
        return render(request, 'base.html')

def status_modif(request):
    print(request)
    if request.method == 'POST':
      print("ca post")
      Status.objects.filter(pk=1).update(status = request.POST.get('status'))
    HttpResponse("Every" , Status.objects.get(pk=1).status,)
    return render(request, 'dashboard.html')
    

def statut(request):
  return HttpResponse(Status.objects.get(pk=1).status);


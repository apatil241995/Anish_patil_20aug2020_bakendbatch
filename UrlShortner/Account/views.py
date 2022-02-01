from django.contrib import messages
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout


@csrf_exempt
def Register(request):
    return render(request, "singin.html")


@csrf_exempt
def singup(request):
    username = request.POST['username']
    email = request.POST['email']
    f_name = request.POST['f_name']
    l_name = request.POST["l_name"]
    pass1 = request.POST['pass1']
    pass2 = request.POST['pass2']
    if pass1 == pass2:
        if User.objects.filter(username=username).exists():
            return HttpResponse('Username taken..', status=400)
        elif User.objects.filter(email=email).exists():
            return HttpResponse('Email taken..', status=400)
        else:
            user = User.objects.create_user(
                username=username,
                email=email,
                first_name=f_name,
                last_name=l_name,
                password=pass1,
            )
            user.save()

        return HttpResponseRedirect('http://127.0.0.1:8000/home/v1/customer/v1/c_login_page/')
    return HttpResponseRedirect('Passwords are not matching..', status=400)


@csrf_exempt
def login(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(username=username, password=password)
        if user is not None:
            login(request, user)
            messages.success(request, "Successfully login")
            return redirect('home')
        else:
            messages.error(request, 'wrong username or password')
            return request('login')
    return HttpResponse(messages.error(request, 'not allowed'))


@csrf_exempt
def logout(request):
    if request.method == "POST":
        logout(request)
        messages.success(request, "Successfully loged out")
    return redirect('home')


def add():
    pass

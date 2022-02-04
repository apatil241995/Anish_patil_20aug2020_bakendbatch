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


# Python3 program to implement
# the above approach

# Function to find the longest
# substring between pair of
# repetitions of the same character
def longestbetweenequalcharacters(S):
    n = len(S)
    res = -1
    diff = -1
    for i in range(n - 1):
        for j in range(n - 1, i, -1):
            if (S[i] == S[j]):
                diff = j - i - 1
                res = max(diff, res)
    return res


# Driver Code
if __name__ == '__main__':
    s = "accabbacc"

    print(longestbetweenequalcharacters(s))

# This code is contributed by doreamon_

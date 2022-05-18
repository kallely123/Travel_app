from django.contrib import messages, auth
from django.contrib.auth.models import User
from django.shortcuts import render, redirect


# Create your views here.
def logout (request):
    auth.logout(request,)
    return redirect('/')

def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = auth.authenticate(username=username,password=password)
        if user is not None:

            auth.login(request,user)
            return redirect('/')
        else:
            messages.info(request, 'Invalid Username or password !!')

            return redirect('login')

    return render(request,'login.html')

def register(request):

    if request.method == 'POST':
        username=request.POST['username']
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        email = request.POST['email']
        password = request.POST['password']
        password2 = request.POST['password2']
        if password == password2:

            if User.objects.filter(username=username).exists():
                messages.info(request, 'User already exist!')
                return redirect('register')
            elif User.objects.filter(email=email).exists():
                messages.info(request, 'email already exist!')
                return redirect('register')
            else:
                user = User.objects.create_user(username=username, first_name=first_name, last_name=last_name,email=email,password=password)
                user.save()
                messages.info(request, 'User created!')

        else:
            messages.info(request, 'opz!!!!! Password not matched try another one ')
            return redirect('register')
        return redirect('login')
    return render(request,'register.html')
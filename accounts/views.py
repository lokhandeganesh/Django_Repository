from django.shortcuts import redirect, render
from django.contrib.auth.models import User,auth
from django.contrib import messages


# Create your views here.


def register(request):
    if request.method == 'POST' :
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        user_name = request.POST['user_name']
        email = request.POST['email']
        password = request.POST['password']
        conf_password = request.POST['conf_password']

        if password == conf_password :
            if User.objects.filter(username = user_name) :
                messages.info(request, 'Username Already Registered')
                return redirect('register')

            else:
                user = User.objects.create_user(
                username = user_name , password = password, 
                email = email, first_name  = first_name,
                last_name = last_name)
                
                user.save()
                messages.info(request, "User Created")
                print("User Created")
                return redirect("login")            

        else:
            messages.info(request,"Password Doesn't Match ")
            print("Password Doesn't Match")
            return redirect("register")                   
        
        return redirect('/')    

    else:
        return render(request, "register.html")

def login(request):
    if request.method =='POST':
        username = request.POST['username']        
        password = request.POST['password']

        user = auth.authenticate(username=username,password=password)
        if user is not None:
            auth.login(request,user)
            return redirect("/")
        else:
            messages.info(request,"invalid credentials")
            print("invalid credentials")
            return redirect("login")            

    else:
        return render(request, 'login.html')   

def logout(request):
    auth.logout(request)
    return redirect('/')

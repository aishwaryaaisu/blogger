from django.contrib.auth import authenticate, login,logout
from django.shortcuts import render,HttpResponse
from django.contrib.auth.models import User
def signin(request):
	if request.method=="POST":
		username = request.POST['username']
		password = request.POST['password']
		user = authenticate(request, username=username, password=password)
		if user is not None:
			login(request, user)

			return HttpResponse("success!")

	return render(request,"login.html")

def logout_user(request):
    logout(request)
    return HttpResponse("logged out successfully")

def signup_user(request):
	if request.method=="POST":
		username=request.POST.get('username',None)
		email=request.POST.get('email')
		password=request.POST.get('password',None)
		user = authenticate(request, username=username,email=email ,password=password)
		if user is None:
			User.objects.create_user(username, email, password)

			return HttpResponse("signup successfully!")
		else:
			return HttpResponse("please check.user might already exist")

	return render(request,"signup.html")



		
		


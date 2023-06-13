from django.shortcuts import render,redirect
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import Add_User
# Create your views here.
def signup(request):
    if request.method=="POST":
        firstname=request.POST["firstname"]
        lastname=request.POST["lastname"]
        username=request.POST["username"]
        phone_number=request.POST["phone-number"]
        email=request.POST["email"]
        password=request.POST["password"]
        state_of_origin=request.POST["state-of-origin"]
        lga=request.POST["lga"]
        country_of_residence=request.POST["country-of-residence"]
        state_of_residence=request.POST["state-of-residence"]
        city=request.POST["city"]
        occupation=request.POST["occupation"]
        place_of_work=request.POST["place-of-work"]
        # confirm_password=request.POST["confirm-password"]
        new_user=Add_User(firstname=firstname, lastname=lastname, username=username, phone_number=phone_number, email=email, password=password, state_of_origin=state_of_origin, lga=lga, country_of_residence=country_of_residence, city=city, occupation=occupation, place_of_work=place_of_work)
        new_user.save()
        user=authenticate(request, username=username, password=password)
        
        
        login(request, user)
        return redirect ("display")
        
        
        
    return render(request, "registration.html")


def login_user(request):
    if request.method=="POST":
        username=request.POST["username"]
        password=request.POST["password"]
        user=authenticate(request, username=username, password=password)
        
        if user is not None:
            login(request, user)
            return redirect ("display")
       
    return render(request, "login.html")
@login_required
def logout_user(request):
    logout(request)
    return redirect("home")
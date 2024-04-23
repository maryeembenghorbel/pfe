from django.contrib.auth import login, authenticate

from django.shortcuts import render, redirect

import os

from django.shortcuts import render

from django.http import JsonResponse

import requests

from pages.forms import ScanForm

from django.shortcuts import render

from .models import User,Role
from django.http import HttpResponseNotFound,HttpResponseServerError,HttpResponse
from django.http import HttpResponseForbidden
from django.contrib.auth.decorators import login_required
from django.urls import reverse_lazy
from django.views.generic.edit import CreateView
from django.db import IntegrityError







 

def login_view(request):    #login

    error = None

 

    if request.method == "POST":

        username = request.POST.get('username')

        password = request.POST.get('password')

 

        # Print username and password

        print("Username:", username)

        print("Password:", password)

 

        user = authenticate(request, username=username, password=password)

        print("User:", user)  # Print the authenticated user

        if user :

            login(request, user)

            return redirect('BASE')  # Redirect to home after successful login

        else:

            error = 'INCORRECT USERNAME OR PASSWORD'

   

    # Handle GET request here

    return render(request, 'login.html', {'error': error})

 

 

def BASE(request):

    return render(request, 'base.html')

 

def vulnerability_trends(request):   #dashbord

    # Retrieve vulnerability trend data (replace with your actual data retrieval logic)

    vulnerability_data = []  # List of tuples (timestamp, count)

    return render(request, 'base.html', {'vulnerability_data': vulnerability_data})

 

def new_scan(request):

    if request.method == 'GET':

        form = ScanForm()

        return render(request, 'scan.html', {'form': form})

 

    elif request.method == 'POST':

        form = ScanForm(request.POST)

        if form.is_valid():

            scan_result = print('hello')

            if scan_result:

                return JsonResponse({'message': 'Scan started successfully.'})

            else:

                return JsonResponse({'error': 'Failed to start the scan.'}, status=500)

        else:

            return render(request, 'scan.html', {'form': form})
        
        
        
        
#acces au nessus via son url

#def new_scan(request):

    # Rediriger vers l'URL de votre instance Nessus Essentials

    #return redirect('https://192.168.110.144:8834')
def user_page(request):
    # Retrieve all users from the database
    mem = User.objects.all()
    
    # Pass the 'mem' variable to the template context
    return render(request, 'user_page.html', {'mem': mem})

def add(request):
    return render(request, 'add.html')

from django.db import IntegrityError

from django.db import IntegrityError

def addrec(request):
    if request.method == 'POST':
        # Handle form submission
        user_name = request.POST.get('user_name')
        email = request.POST.get('email')
        password = request.POST.get('password')
        role_id = request.POST.get('role_id')

        try:
            role = Role.objects.get(pk=role_id)
        except Role.DoesNotExist:
            return HttpResponse("Role ID does not exist", status=404)

        try:
            # Create and save new user object
            new_user = User(user_name=user_name, email=email, password=password, role_id=role_id)
            new_user.save()
            print(new_user)
        

            # Redirect to home page after successful user creation
            return redirect("/")  

        except Exception as e:
            print(f"Error occurred while creating user: {e}")
            return HttpResponse("Error occurred while adding user. Please try again.", status=500)

    else:
        # Render the form for GET requests
        return render(request, "add.html")
def delete(request, id):
    # Check if the authenticated user is a supervisor
    if not request.user.is_supervisor:
        return HttpResponseForbidden("You do not have permission to delete users.")

    # Proceed with deletion logic
    mem = User.objects.get(id=id)
    mem.delete()
    return redirect("/")

@login_required
def update(request, id):
    # Check if the authenticated user is a supervisor
    if not request.user.is_supervisor:
        return HttpResponseForbidden("You do not have permission to update users.")

    # Proceed with update logic
    mem = User.objects.get(id=id)
    return render(request, 'update.html', {'mem': mem})

def uprec(request, id):
    if request.method == 'POST':
        x = request.POST.get('name')
        y = request.POST.get('email')
        z = request.POST.get('password')
        w = request.POST.get('role_id')
        
        # Assuming 'role' is the ForeignKey field, you need to get the Role object
        # You may need to adjust this part based on how you handle roles in your application
        role = Role.objects.get(id=w)

        # Update the existing User object
        mem = User.objects.get(id=id)
        mem.user_name = x
        mem.email = y
        mem.password = z
        mem.role = role
        mem.save()

        return redirect("/user_page")
    else:
        # Handle GET request if needed
        pass
    
class UserCreateView(CreateView):
    model = User
    fields = ['user_name', 'email', 'password', 'role_id']
    success_url = reverse_lazy('user_page')



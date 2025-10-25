import re
from django.shortcuts import render, redirect
from httplib2 import Http
from .models import *
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required

def recipes(request):
    if request.method == "POST":
        data = request.POST
        
        recipe_image = request.FILES.get('recipe_image')
        recipe_name = data.get('recipe_name')
        recipe_description = data.get('recipe_description')
        
        Recipe.objects.create(
			recipe_name = recipe_name,
			recipe_description = recipe_description,
			recipe_image = recipe_image
		)
        
        print(recipe_name,"\n")
        print(recipe_description)
        
        return redirect('/recipes')
    
    queryset = Recipe.objects.all()
    search_term = request.GET.get('search')
    
    if search_term:
        queryset = queryset.filter(recipe_name__icontains = search_term)
        
    context = {
        'page' : 'Recipes',
        'recipes' : queryset,
        'search_term': search_term or ''
        }
    return render(request, 'recipes.html', context=context)


@login_required(login_url='/login/')
def delete_recipe(request, id):
    queryset = Recipe.objects.get(id=id)
    queryset.delete()
    messages.success(request, "Recipe deleted successfully.")
    return redirect('/recipes/')


@login_required(login_url='/login/')
def update_recipe(request, id):
    queryset = Recipe.objects.get(id=id)
    context = {'page': 'Update recipes', 'recipe':queryset}
    
    if request.method == 'POST':
        data = request.POST
        recipe_image = request.FILES.get('recipe_image')
        recipe_name = data.get('recipe_name')
        recipe_description = data.get('recipe_description')
        
        queryset.recipe_name = recipe_name
        queryset.recipe_description = recipe_description
        
        if recipe_image:
            queryset.recipe_image = recipe_image
        queryset.save()
        
        messages.success(request, "Recipe updated successfully!") 
        return redirect('/recipes/')
    return render(request, 'update_recipes.html', context=context)

def login_page(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        
        if not User.objects.filter(username=username).exists():
            messages.error(request, "Username does not exist")
            return render(request, 'login.html', {'page': 'Login'})
    
        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            messages.success(request, f"Welcome back, {user.username}!")
            return redirect('/recipes/')
        else:
            messages.error(request, "Invalid username or password")
            return render(request, 'login.html', {'page': 'Login'})

    return render(request, 'login.html', context={'page': 'Login'})

def register_page(request):
    if request.method == "POST":
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        username = request.POST.get('username')
        password = request.POST.get('password')
        confirm_password = request.POST.get('confirm_password')
        
        if password != confirm_password:
            return HttpResponse("Passwords do not match")
        
        if User.objects.filter(username=username).exists():
            messages.info(request, 'Username already taken')
            return redirect('/register/')

        user = User.objects.create(
            first_name=first_name,
            last_name=last_name,
            username=username
        )
        user.set_password(password)
        #'pbkdf2_sha256$1000000$nxTINa7goq9PYWG2DCw8fI$gZPFZDgzURCfVicYYj0SXJfvEtd0j0lB+NkeuObHyfE=' mat khau da duoc ma hoa
        user.save()

        return redirect('/login/')
    
    return render(request, 'register.html',context={'page':'Register'})

def logout_page(request):
    logout(request)
    messages.success(request, "You have been logged out successfully.")
    return redirect('/login/')
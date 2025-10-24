from django.shortcuts import render, redirect
from httplib2 import Http
from .models import *
from django.http import HttpResponse
# Create your views here.
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

def delete_recipe(request, id):
    queryset = Recipe.objects.get(id=id)
    queryset.delete()
    return redirect('/recipes/')

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
        return redirect('/recipes/')
        
    return render(request, 'update_recipes.html', context=context)

def login_page(request):
    return render(request, 'login.html')

def register_page(request):
    return render(request, 'register.html')
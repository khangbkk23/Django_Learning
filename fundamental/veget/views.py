from django.shortcuts import render, redirect
from .models import *
# Create your views here.
def recipes(request):
    context = {'page' : 'Recipes'}
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
    return render(request, 'recipes.html', context=context)
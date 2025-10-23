from django.shortcuts import render

# Create your views here.
def recipes(request):
    context = {'page' : 'Recipes'}
    if request.method == "POST":
        data = request.POST
        
        recipe_image = request.FILES.get('recipe_image')
        recipe_name = data.get('recipe_name')
        recipe_description = data.get('recipe_description')
        print(recipe_name,"\n")
        print(recipe_description)
    return render(request, 'recipes.html', context=context)
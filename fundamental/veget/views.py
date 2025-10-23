from django.shortcuts import render

# Create your views here.
def recipes(request):
    context = {'page' : 'Recipes'}
    return render(request, 'recipes.html', context=context)
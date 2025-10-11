from django.shortcuts import render
from django.http import HttpResponse
from httplib2 import Http

# Create your views here.

def home(request):
    return HttpResponse(""" <h1> Hey I am a Django Server. </h1>
                        <p> Hey this is coming from Django server. Let's chill with coding Django. </p>
                        <hr>
                        <h3 style = "color:red"> Hope you and me loving it :)) </h3>
                        """)

# Connect with html file
def about(request):
    peoples =[
        {'name':'Bui Tran Duy Khang', 'age':20, 'role':'Son'},
        {'name':'Bui Quoc Nam', 'age':47, 'role':'Daddy'},
        {'name':'Tran Hong Van', 'age': 45, 'role':'Mommy'},
        {'name':'Bui Tran Nhat Duy', 'age':9, 'role':'Son'}
    ]
    text = """In my mind, I love my family very much!"""
        
    return render(request, "home/index.html", context={
    'peoples': peoples,
    'text': text
    })

    
def success_page(request):
    print("*" * 10)
    return HttpResponse(""" <h1> Hey this is a Success page </h1>
                        """)
from django.shortcuts import render
from django.http import HttpResponse
from httplib2 import Http
from datetime import date

# Create your views here.

def home(request):
    return HttpResponse(""" <h1> Hey I am a Django Server. </h1>
                        <p> Hey this is coming from Django server. Let's chill with coding Django. </p>
                        <hr>
                        <h3 style = "color:red"> Hope you and me loving it :)) </h3>
                        """)

# Connect with html file
def about(request):
    peoples = [
        {'name':'Bui Tran Duy Khang', 'dob':'08/01/2005', 'role':'Son'},
        {'name':'Bui Quoc Nam', 'dob':'16/12/1978', 'role':'Daddy'},
        {'name':'Tran Hong Van', 'dob':'31/01/1980', 'role':'Mommy'},
        {'name':'Bui Tran Nhat Duy', 'dob':'01/08/2016', 'role':'Son'}
    ]

    today = date.today()

    for person in peoples:
        if 'dob' in person and 'age' not in person:
            day, month, year = map(int, person['dob'].split('/'))
            dob_date = date(year, month, day)
            age = today.year - dob_date.year - ((today.month, today.day) < (dob_date.month, dob_date.day))

            person['age'] = age

    context = {
        'peoples': peoples,
        'text': 'In my mind, I love my little family very much!'
    }
    
    return render(request, 'home/index.html', context)

    
def success_page(request):
    print("*" * 10)
    return HttpResponse(""" <h1> Hey this is a Success page </h1>
                        """)
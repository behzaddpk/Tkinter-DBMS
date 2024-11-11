from cmath import log
from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.


data = [
    {'id':'1', 'name':'behzad Sarwar', 'age': '25'},
    {'id':'2','name':'shabaz Sarwar', 'age': '25'},
    {'id':'3','name':'ijaz Sarwar', 'age': '25'},
]


def home(request):
    return render(request, 'home.html', {'data': data})

 
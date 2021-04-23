from django.http import HttpResponse
from django.shortcuts import render

def index(request):
    values = {'name':'Prayo', 'age':22, 'city':'pune'}
    return render(request, 'home.html', values)

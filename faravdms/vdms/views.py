from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse

from vdms.models import Student
# Create your views here.
def login(request):
    return render(request,"login.html",{'name':'Samuel'})

def index(request):
    return render(request,"index.html",{'name':'Samuel'})




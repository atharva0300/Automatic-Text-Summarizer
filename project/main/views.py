from django.shortcuts import render

from django.http import HttpResponse
from django.shortcuts import render


# Create your views here.
def home_view(request) :
    
    return render(request , 'home.html' , {})


def try_view(request) :
    return render(request , 'try.html' , {})
   


def select_algo(request) : 
    if request.method=='GET' : 
        algo = request.body.cleaned_data()

        return render(request , 'try.html' , {'message' : algo})
    
    else : 
        return render(request , 'try.html' , {'message' : 'Not received'})
    
    

from django.shortcuts import render

# Create your views here.
def conditions(request):
    d ={'a':20,'b':30,'c':10}
    return render(request,'conditions.html',context=d)

def nested_if(request):
    d ={'a':40,'b':30,'c':70}
    return render(request,'nested_if.html',context=d)

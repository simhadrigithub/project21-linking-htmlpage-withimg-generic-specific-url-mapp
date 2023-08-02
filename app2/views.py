from django.shortcuts import render

# Create your views here.
d={'benefits':['very fast digestion','assists the muscles','greate for vision','brain and mental health']}

def grapes(request):
    return render(request,'grapes.html',context=d)
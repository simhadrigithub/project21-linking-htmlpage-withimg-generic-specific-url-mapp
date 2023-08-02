from django.shortcuts import render

# Create your views here.
d={'benefits':['orange  have vitamin c','orange can improve brain health','orange can reduce kidney stones']}
def orange(request):
    return render(request,'orange.html',context=d)
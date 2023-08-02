from django.shortcuts import render

# Create your views here.
d={'fruit':['color:red','symbol:love','advantage:to reduce cancer desease',]}
def apples(request):
    return render(request,'apples.html',context=d)

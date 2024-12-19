from django.shortcuts import render

# Create your views here.
def guess(request):
    return render(request,'index.html')
def resultt(request):
    return render(request,'results.html')
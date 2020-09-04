from django.shortcuts import render

# Create your views here.
def f_py(request):
    return render(request,'fees/f1.html')
def f_dj(request):
    return render(request,'fees/f2.html')

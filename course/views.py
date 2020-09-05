from django.shortcuts import render
from datetime import datetime
def l_py(request):
    coursename="python"
    duration="7 days"
    seet="10 seets"
    dt=datetime.now()
    py_data ={'cname':coursename,'du':duration,'st':seet,'d':dt}

    return render(request,'course/c1.html',py_data)
def l_dj(request):
    coursename = "django"
    duration = "7 days"
    seet = "10 seets"
    Dj_data = {'cname': coursename, 'du': duration, 'st': seet}

    return render(request,'course/c2.html',Dj_data)



# Create your views here.

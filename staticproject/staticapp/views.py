from django.shortcuts import render
from .models import A, new


# Create your views here.
def static(request):
    obj=A.objects.all()
    d=new.objects.all()
    return render(request,'index.html',{'result':obj ,'r': d})




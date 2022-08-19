from django.shortcuts import render
from .models import Datas

# Create your views here.
def home(request):
    return render(request, 'home.html') 

def tfs(request):
    return render(request,'tfs.html')

def ShareInfo(request):
    if request.method=="POST":
        name=request.POST['name']
        don=request.POST['don']
        phn=request.POST['phn']
        loc=request.POST['loc']
        datas=Datas(name=name,don=don,phn=phn,loc=loc)
        datas.save()
        return render(request, 'tfs.html')
    return render(request,'ShareInfo.html') 

def login(request):
    return render(request, 'login.html') 

def verify(request):
    val1 = request.GET['username']
    val2 = request.GET['email'] 
    if(val1=='suvith' and val2=='abc@gmail.com'):
        card = Datas.objects.all()
        return render(request,'fin.html',{'cards':card})
    else:
        return render(request,'thank.html')


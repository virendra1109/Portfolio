from django.shortcuts import render,redirect
from .models import Contact


# Create your views here.
def index(request):
    return render(request, 'index.html')
def home(request):
    if request.method == 'POST':
        nm=request.POST.get('name')
        em=request.POST.get('email')
        sub=request.POST.get('subject')
        msg=request.POST.get('message')
        data=Contact(name=nm,email=em,subject=sub,message=msg)
        data.save()
        return redirect('index')
    return render(request,'index.html')
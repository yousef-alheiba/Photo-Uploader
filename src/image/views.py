from django.shortcuts import render,redirect
from .models import *

from .forms import *

# Create your views here.

def listphoto(request):
    photos = Photo.objects.all()
    
    context={
        'photos':photos,
    }
    return render(request,'image/listphoto.html',context)
def addphoto(request):
    form = PhotoForm()
    if request.method=='POST':
        form= PhotoForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
        return redirect('/')
    context={
        'form':form
    }
    return render(request,'image/addphoto.html',context)
def deletephoto(request,pk):
    photo = Photo.objects.get(id=pk)
    if request.method=='POST':
        photo.delete()
        return redirect('/')
    context={
        'photo':photo
    }
    return render(request,'image/deletephoto.html',context)
def updatephoto(request,pk):
    photo = Photo.objects.get(id=pk)
    form = PhotoForm(instance=photo)
    if request.method=='POST':
        form = PhotoForm(request.POST, request.FILES,instance=photo)
        if form.is_valid():
            form.save()
            return redirect('/')
    context={
        'form':form
    }
    return render(request,'image/updatephoto.html',context)

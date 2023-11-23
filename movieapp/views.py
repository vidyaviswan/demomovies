from django.contrib import messages
from django.http import HttpResponse
from django.shortcuts import render, redirect
from.models import Movie
from .forms import MovieForm



def index(request):
    movie=Movie.objects.all()
    context={
        'movielist':movie
    }
    return render(request,'index.html',context)
def detail(request,movieid):
    movie=Movie.objects.get(id=movieid)
    return render(request ,"detail.html",{'movie' :movie})
    #return HttpResponse("This is movie no %s" %movieid)
def add_movie(request):
    if request.method=='POST':
        name=request.POST.get('name',)
        des = request.POST.get('desc',)
        year = request.POST.get('year',)
        img = request.FILES['img']
        movie=Movie(name=name,des=des,year=year,img=img)
        movie.save()

    return render(request, 'add.html')
    messages.info(request, "Data Added Successfully.....")


def update(request,id):
    movie = Movie.objects.get(id=id)
    form=MovieForm(request.POST or None,request.FILES,instance=movie)
    if form.is_valid():
        form.save()
        return redirect('/')
    return render(request,'edit.html',{'form':form,'movie':movie})


def delete(request,id):
    if request.method == 'POST':
        movie = Movie.objects.get(id=id)
        movie.delete()
        return redirect('/')
    return render(request,'delete.html')
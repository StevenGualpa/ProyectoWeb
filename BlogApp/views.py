from django.shortcuts import render
from BlogApp.models import Categorias, Post
# Create your views here.


def blog(request):
    postss=Post.objects.all()
    return render(request,"BlogApp/blog.html",{"posts":postss})

def categoria(request, categoria_id):
    
    categoria_=Categorias.objects.get(id=categoria_id)
    postss=Post.objects.filter(categorias=categoria_) #verbose_name_plural en models
    #postss=Post.objects.all()
    return render(request,"BlogApp/categorias.html",{"categoria":categoria_ ,"posts":postss})
from django.shortcuts import render
from django.http import HttpResponse
from . models import Item
def index(request):
    item = Item.objects.all()
    return render(request,'index.html',{'item':item})



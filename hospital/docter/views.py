from django.shortcuts import render, redirect
from django.http import HttpResponse
from . models import Doctor, Department,Booking
from . forms import BookingForm
def index(request):
    return render(request,'index.html')
def doctor(request):
    doctor=Doctor.objects.all()
    return render(request,'doctor.html',{'doctor':doctor})
def department(request):
    department=Department.objects.all()
    return render(request,'department.html',{'department':department})
def booking(request):
    form = BookingForm()
    if request.method=='POST':
        form=BookingForm(request.POST)
        if form.is_valid():
            form.save()
            redirect('index')
    return render(request,'booking.html',{'form' :form})
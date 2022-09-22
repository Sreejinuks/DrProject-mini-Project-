from django.http import HttpResponse
from django.shortcuts import render

from drapp.forms import BookingForm
from drapp.models import Department, Doctor


# Create your views here.
def index(request):
    return render(request,'index.html')
def about(request):
    return render(request,'about.html')

def booking(request):
    if request.method == "POST":
        form = BookingForm(request.POST)
        if form.is_valid():
            form.save()
            return render(request, 'confirmation.html')
    form = BookingForm()
    dict_form = {
        'form': form
    }
    return render(request, 'booking.html', dict_form)

def doctor(request):
    dict_docs = {
        'doctor': Doctor.objects.all()
    }
    return render(request, 'doctor.html', dict_docs)

def department(request):
    dict_dept={
            'dept':Department.objects.all()
        }
    return render(request,'department.html',dict_dept)
def contact(request):
    return render(request,'contact.html')
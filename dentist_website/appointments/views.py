from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import Appointment
from .forms import AppointmentForm
from django.contrib.auth.forms import UserCreationForm


def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            Patient.objects.create(user=user)
            return redirect('login')
    else:
        form = UserCreationForm()
    return render(request, 'appointments/signup.html', {'form': form})


@login_required
def home(request):
    return render(request, 'appointments/home.html')

@login_required
def book_appointment(request):
    if request.method == 'POST':
        form = AppointmentForm(request.POST)
        if form.is_valid():
            appointment = form.save(commit=False)
            appointment.patient = request.user.patient
            appointment.save()
            return redirect('appointments:list')
    else:
        form = AppointmentForm()
    
    return render(request, 'appointments/book_appointment.html', {'form': form})

@login_required
def list_appointments(request):
    appointments = Appointment.objects.filter(patient=request.user.patient)
    return render(request, 'appointments/list_appointments.html', {'appointments': appointments})

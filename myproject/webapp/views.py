from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.forms import UserCreationForm
from .forms import CustomUserCreationForm, ReservationForm
from django.contrib.auth import authenticate, login
from django.views.decorators.csrf import csrf_protect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from webapp.models import Addroom, Reservation
from django.urls import reverse 

def index(request):
    return render(request, 'index.html')
 
def loginn(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('booking')
        else:
            # หากไม่มี user หรือ password ผิดพลาด แสดงคำเตือน
            error_message = "ชื่อผู้ใช้หรือรหัสผ่านไม่ถูกต้อง"
            return render(request, 'loginn.html', {'error_message': error_message})
    else:
        return render(request, 'loginn.html')
 
def regis(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('loginn')  # หรือไปยังหน้าอื่นตามที่คุณต้องการหลังจากลงทะเบียนสำเร็จ
        else:
            # ในกรณีที่ฟอร์มไม่ถูกต้อง แสดงข้อความผิดพลาด
            error_message = "เกิดข้อผิดพลาด โปรดลองอีกครั้ง"
            return render(request, 'regis.html', {'form': form, 'error_message': error_message})
    else:
        form = CustomUserCreationForm()
    return render(request, 'regis.html', {'form': form})

@login_required
def result(request):
    all_result = Reservation.objects.all()
    return render(request, 'result.html', {"all_result": all_result})
 
@login_required
def booking(request):
    addroom = Addroom.objects.all()
    return render(request, 'booking.html',{"addroom":addroom})

# def booking2(request, roomm ):
#     return render(request, 'booking2.html', {'roomm' : roomm})

def bookingcreate(request ,roomm):
    addroom = Addroom.objects.all()
    if request.method == 'POST':
        form = ReservationForm(request.POST)
        if form.is_valid():
            roomm = form.cleaned_data['roomm']
            reservation_date = form.cleaned_data['reservation_date']
            reservation_time = form.cleaned_data['reservation_time']
            reservation_timestop = form.cleaned_data['reservation_timestop']
            
            # ตรวจสอบว่ามีการจองห้องในช่วงเวลาเดียวกันหรือไม่
            if Reservation.objects.filter(roomm=roomm, reservation_date=reservation_date).exists():
                existing_reservation = Reservation.objects.get(roomm=roomm, reservation_date=reservation_date)
                if (reservation_time >= existing_reservation.reservation_time and
                        reservation_time <= existing_reservation.reservation_timestop) or \
                   (reservation_timestop >= existing_reservation.reservation_time and
                        reservation_timestop <= existing_reservation.reservation_timestop):
                    form.add_error(None, "This room is already booked at this time.")
                    return render(request, 'bookingcreate.html', {'form': form})

            form.save()
            return redirect('result')  # หรือไปยังหน้าที่คุณต้องการ
    else:
        form = ReservationForm(initial={'roomm': roomm})
    return render(request, 'bookingcreate.html', {'form': form, 'roomm':roomm, "addroom":addroom})
# Create your views here.
 
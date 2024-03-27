# app_reserve/forms.py
 
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Reservation
from django.core.exceptions import ValidationError

class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email', 'password1', 'password2', 'phone')
    first_name = forms.CharField(max_length=30, required=False)
    last_name = forms.CharField(max_length=30, required=False)
    email = forms.EmailField(max_length=254, help_text='Required. Inform a valid email address.')
    phone = forms.CharField(max_length=15, required=False)
 


class ReservationForm(forms.ModelForm):
    class Meta:
        model = Reservation
        fields = ['roomm', 'user', 'reservation_date', 'reservation_time', 'reservation_timestop']
        widgets = {
            'reservation_date': forms.DateInput(attrs={'type': 'date'}),
            'reservation_time': forms.TimeInput(attrs={'type': 'time'}),
            'reservation_timestop': forms.TimeInput(attrs={'type': 'time'}),
        }

    def clean(self):
        cleaned_data = super().clean()
        roomm = cleaned_data.get("roomm")
        reservation_date = cleaned_data.get("reservation_date")
        reservation_time = cleaned_data.get("reservation_time")
        reservation_timestop = cleaned_data.get("reservation_timestop")

        # ตรวจสอบว่ามีการจองห้องในวันที่และเวลาเดียวกันหรือไม่
        if Reservation.objects.filter(roomm=roomm, reservation_date=reservation_date).exists():
            existing_reservation = Reservation.objects.get(roomm=roomm, reservation_date=reservation_date)
            if (reservation_time >= existing_reservation.reservation_time and
                    reservation_time <= existing_reservation.reservation_timestop) or \
               (reservation_timestop >= existing_reservation.reservation_time and
                    reservation_timestop <= existing_reservation.reservation_timestop):
                raise ValidationError("This room is already booked at this time.")

        return cleaned_data

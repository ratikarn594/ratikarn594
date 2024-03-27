from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('loginn/', views.loginn, name='loginn'),
    path('regis/', views.regis, name='regis'),
    path('booking/', views.booking, name='booking'),
    path('result/', views.result, name='result'),
    path('web/logout/', auth_views.LogoutView.as_view(next_page='loginn'), name='logout'),
    # path('booking2/<str:roomm>/', views.booking2, name='booking2'),
    path('bookingcreate/<str:roomm>/', views.bookingcreate, name='bookingcreate'),
]

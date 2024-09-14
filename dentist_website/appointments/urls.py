from django.urls import path
from . import views

app_name = 'appointments'

urlpatterns = [
    path('', views.home, name='home'),
    path('book/', views.book_appointment, name='book'),
    path('list/', views.list_appointments, name='list'),
    path('signup/', views.signup, name='signup'),

]

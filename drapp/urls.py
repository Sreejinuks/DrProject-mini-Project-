from drapp import views
from django.urls import path
urlpatterns = [
    path('',views.index,name='home'),
    path('about',views.about,name='about'),
    path('booking',views.booking,name='booking'),
    path('doctor',views.doctor,name='doctor'),
    path('department',views.department,name='department'),
    path('contact',views.contact,name='contact'),
]
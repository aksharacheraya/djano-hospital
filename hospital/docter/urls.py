from django.urls import path
from.import views
urlpatterns=[
    path('',views.index,name='index'),
    path('doctor/',views.doctor,name='doctor'),
    path('department/',views.department,name='department'),
    path('booking/',views.booking,name='booking'),
]
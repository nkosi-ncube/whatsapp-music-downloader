from django.urls import path
from . import views

urlpatterns=[
    path('',views.bot,name='bot'),
    path('feedback/',views.feedback,name ='feedback')
]
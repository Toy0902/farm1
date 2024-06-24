from django.urls import path
from .views import *
urlpatterns = [
    path('', index, name='index'),
    path('meeting_details/', meeting_details, name="meeting_details"),
    path('meetings/', meetings, name="meetings"),
    path('rasm_detel/<int:id>/', index_detel, name="rasm_detel"),
    path('rasm_detel2/<int:id>/', index_detel2, name="rasm_detel2")
]

from rest.views import home,person
from django.urls import path

urlpatterns=[
    path('home/',home),
    path('person/',person)
]
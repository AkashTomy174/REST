from rest.views import home,person,persons
from django.urls import path

urlpatterns=[
    path('home/',home),
    path('person/',person),
    path('persons/',persons.as_view())
]
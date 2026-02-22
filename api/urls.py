from rest.views import home,PeopleViewSet#,person,persons
from django.urls import path,include

from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register('people', PeopleViewSet )





urlpatterns=[
    path('',include(router.urls)),
    path('home/',home),
    # path('person/',person),
    # path('persons/',Persons.as_view())
]

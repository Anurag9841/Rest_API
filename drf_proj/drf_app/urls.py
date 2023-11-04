from django.urls import path
from .views import test,stud,drinks,drinks_det
urlpatterns = [
    path('',test.as_view(),name='test'),
    path('student',stud,name='student'),
    path('drink',drinks.as_view(),name='drink'),
    path('drink/<int:id>',drinks_det,name='drinks_det')
]
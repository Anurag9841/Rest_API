from django.urls import path
from .views import test,stud
urlpatterns = [
    path('',test.as_view(),name='test'),
    path('student',stud,name='student')
]
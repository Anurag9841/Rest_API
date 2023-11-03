from django.shortcuts import render
from django.http import JsonResponse
from rest_framework.views import APIView
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import student
from .seralizers import studentSerializers
# Create your views here.
class test(APIView):
    def get(self,request,*args,**kwargs):
        students = student.objects.all()
        serializer = studentSerializers(students, many=True)
        return Response(serializer.data)
    def post(self,request,*args,**kwargs):
        serializer = studentSerializers(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)

@api_view(['GET','POST'])
def stud(request):
    if request.method == 'GET':
        students = student.objects.all()
        serializer = studentSerializers(students,many=True)
        return Response(serializer.data)
    elif request.method == 'POST':
        serializer = studentSerializers(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)





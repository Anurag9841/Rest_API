from django.shortcuts import render,redirect
from django.http import JsonResponse
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import student,drink
from .seralizers import studentSerializers,drinkSerializers
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

class drinks(APIView):
    def get(self,request,*args,**kwargs):
        soft_drink = drink.objects.all()##get data from data base
        serializer = drinkSerializers(soft_drink,many=True)## serialize them
        return Response(serializer.data)## display

    def post(self,request,*args,**kwargs):
        serializer = drinkSerializers(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)

@api_view(['GET','PUT','DELETE'])

def drinks_det(request,id):
    try:
        drinks = drink.objects.get(id=id)
    except drink.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    if request.method == "GET":
        serializer = drinkSerializers(drinks)
        return Response(serializer.data)

    if request.method == 'PUT':
        seralizer = drinkSerializers(drinks,data = request.data)
        if seralizer.is_valid():
            seralizer.save()
            return Response(seralizer.data)
        return Response(seralizer.errors)

    if request.method == 'DELETE':
        drinks.delete()
        return Response(status.HTTP_204_NO_CONTENT)







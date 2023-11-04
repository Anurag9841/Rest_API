from rest_framework import serializers
from .models import student,drink

class studentSerializers(serializers.ModelSerializer):
    class Meta:
        model = student
        fields = ['name','age']

class drinkSerializers(serializers.ModelSerializer):
    class Meta:
        model = drink
        fields = ['name','description','price']
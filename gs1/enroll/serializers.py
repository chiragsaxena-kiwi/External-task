from .models import Employee
from rest_framework import serializers


class EmployeeSerializer(serializers.ModelSerializer):
    name=serializers.CharField(max_length=30)
    email=serializers.EmailField(max_length=30)
    password=serializers.CharField(max_length=30)
    phone=serializers.CharField(max_length=30)


    class Meta:
          model = Employee
          fields = ('name','email','password','phone')

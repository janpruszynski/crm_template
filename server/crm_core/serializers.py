from rest_framework import serializers
from crm_core.models import Employee

class EmployeeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Employee
        fields = '__all__' #('id', 'first_name', 'last_name', 'phone', 'email', 'position')

from crm_core.models import Employee
from crm_core.serializers import EmployeeSerializer
from rest_framework import generics

class EmployeeListCreate(generics.ListCreateAPIView):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer

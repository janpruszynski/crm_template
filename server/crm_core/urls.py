from django.urls import path, include
from . import views

urlpatterns = [
    path('api/employees/', views.EmployeeListCreate.as_view()),
]

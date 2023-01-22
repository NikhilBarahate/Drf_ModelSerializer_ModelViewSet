from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.response import Response
from app1.models import Students
from app1.serializers import StudentSerializer

# Create your views here.
class StudentDetails(viewsets.ModelViewSet):
    serializer_class = StudentSerializer
    queryset = Students.objects.all()
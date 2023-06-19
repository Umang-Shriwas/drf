from django.shortcuts import render
from .models import Student
from api.serializers import StudentSerializer
from rest_framework.renderers import JSONRenderer, JSONOpenAPIRenderer
from django.http import HttpResponse

# Create your views here.

def student_details(request):
    stu = Student.objects.get(id = 1)
    serializer = StudentSerializer(stu)
    json_data = JSONRenderer().render(serializer.data)
    print(json_data)
    return HttpResponse(json_data, content_type='application/json')
    
from student.models import Student
from student.serializers import StudentSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework import mixins
from rest_framework import generics

# Create your views here.

class MyView(generics.GenericAPIView,
             mixins.ListModelMixin,
             mixins.DestroyModelMixin,
             mixins.CreateModelMixin,
             mixins.RetrieveModelMixin,
             mixins.UpdateModelMixin):

    queryset = Student.objects.all()
    serializer_class = StudentSerializer

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)
    
    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)
    
    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)

    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)
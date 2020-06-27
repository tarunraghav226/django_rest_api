from student.models import Student, Subjects
from student.serializers import StudentSerializer, SubjectSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework import mixins
from rest_framework import generics

# Create your views here.

class StudentView(generics.GenericAPIView,
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
    
    def get(self, request, pk=-1, *args, **kwargs):
        if pk==-1:
            queryset = Student.objects.all()
            return self.list(request, *args, **kwargs)
        else:
            queryset = Student.objects.get(id=pk)
            return self.retrieve(request, *args, **kwargs)

    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)

class SubjectView(generics.GenericAPIView,
                  mixins.ListModelMixin,
                  mixins.UpdateModelMixin,
                  mixins.DestroyModelMixin,
                  mixins.CreateModelMixin):
    queryset = Subjects.objects.all()
    serializer_class = SubjectSerializer

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)
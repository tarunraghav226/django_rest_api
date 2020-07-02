from rest_framework import serializers
from .models import Student, Subjects
from django.contrib.auth.models import User

class StudentSerializer(serializers.ModelSerializer): 
    user = serializers.ReadOnlyField(source='user.id')  
    class Meta:
        model = Student
        fields = '__all__'

class SubjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Subjects
        fields = ['student', 'subject_name']

class UserSerializer(serializers.ModelSerializer):
    student = serializers.PrimaryKeyRelatedField(many=True, queryset=Student.objects.all())

    class Meta:
        model = User
        fields = ['id', 'username', 'student']
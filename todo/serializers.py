from .models import User, Task
from djoser.serializers import UserCreateSerializer
from rest_framework import serializers


class UserSerializer(UserCreateSerializer):
    class Meta(UserCreateSerializer.Meta):
        model = User
        fields = ('id', 'email', 'name', 'password')

class TaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = ('id', 'title', 'description', 'is_completed', 'user', 'deadline_date', 'is_notific')
        extra_kwargs = {
            'deadline_date': {'required': True}
        }
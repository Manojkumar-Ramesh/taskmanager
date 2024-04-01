from  task.models import Task
from rest_framework import serializers
from django.contrib.auth.models import User


class TaskSerializers(serializers.ModelSerializer):
    class Meta:
        model=Task
        fields='__all__'
        read_only_fields=["id","assigned_date"]

class Userserializer(serializers.ModelSerializer):
    class Meta:
        model=User
        fields=["id","username","email","password"]
        read_only_fields=["id"]

    def create(self, validated_data): # overiding model create method in modelserializer
        return User.objects.create_user(**validated_data)
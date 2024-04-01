from django.shortcuts import render
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView

from task.models import Task
from task.serializer import TaskSerializers,Userserializer
from rest_framework import authentication,permissions




class TaskViewSetView(ViewSet):
    def list(self,request,*args,**kwargs):
        qs=Task.objects.all()
        serializer_instance=TaskSerializers(qs,many=True)
        return Response(data=serializer_instance.data,status=status.HTTP_200_OK)

    def create(self,request,*args,**kwargs):
        data=request.data
        serializer_instance=TaskSerializers(data=data)
        if serializer_instance.is_valid():
            serializer_instance.save()
            # task.object.create(**serializer_instance.validated_data)
            return Response(data=serializer_instance.data,status=status.HTTP_201_CREATED)
        return Response(data=serializer_instance.errors,status=status.HTTP_400_BAD_REQUEST)
    
    def retrieve(self,request,*args,**kwargs):
        id=kwargs.get("pk")
        task_obj=Task.objects.get(id=id)
        serializer_instance=TaskSerializers(task_obj)
        return Response(data=serializer_instance.data,status=status.HTTP_200_OK)
    
    def update(self,request,*args,**kwargs):
        
        id=kwargs.get("pk")
        qs=Task.objects.get(id=id)
        serializer_instance=TaskSerializers(data=request.data,instance=qs)
        if serializer_instance.is_valid():
            serializer_instance.save()
            return Response(data=serializer_instance.data,status=status.HTTP_200_OK)
        return Response(data=serializer_instance.errors,status=status.HTTP_400_BAD_REQUEST)
    
    def destroy(self,request,*args,**kwargs):
        id=kwargs.get("pk")
        Task.objects.get(id=id).delete()
        return Response(data={"message":"deleted"},status=status.HTTP_200_OK)

class UserView(APIView):
    def post(self,request,*args,**kwargs):
        serializer_instance=Userserializer(data=request.data)
        if serializer_instance.is_valid():
            serializer_instance.save()
            return Response(data=serializer_instance.data,status=status.HTTP_200_OK)
        return Response(data=serializer_instance.errors,status=status.HTTP_400_BAD_REQUEST)

    
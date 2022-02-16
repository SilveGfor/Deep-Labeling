from django.shortcuts import render

from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import generics, status
from django.http import HttpResponse

import json

from Backend.serializers import UsersSerializer

from Backend.models import User, Project


class Authorization(APIView):

    def post(self, request):
        #print(request.data)
        data = json.loads(request.body.decode('utf-8'))
        user_email = data['email']
        user_password = data['password']
        user = User.objects.filter(email=user_email).first()
        users = User.objects.all()
        #print(users)

        project = Project.objects.filter()
        #print(str(project))

        serializer = UsersSerializer(data=request.data)
        #if serializer.is_valid():
        if user.password == user_password:
            return Response({"status": "success"})
        else:
            return Response({"status": "incorrect_password"})
        return Response(serializer.data, status=status.HTTP_400_BAD_REQUEST)

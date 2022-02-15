from django.shortcuts import render

from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import generics, status
from django.http import HttpResponse

from Backend.serializers import UsersSerializer

from Backend.models import User, Project


class Authorization(APIView):

    def post(self, request):
        #print(request.data)
        user_email = request.data.get('email')
        user_password = request.data.get('password')
        user = User.objects.get(email=user_email)
        users = User.objects.all()
        #print(users)

        project = Project.objects.filter()
        #print(str(project))

        serializer = UsersSerializer(data=request.data)
        if serializer.is_valid():
            if user.password == user_password:
                return Response({"status": "success"})
            else:
                return Response({"status": "incorrect_password"})
        return Response(serializer.data, status=status.HTTP_400_BAD_REQUEST)

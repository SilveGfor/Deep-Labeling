from django.shortcuts import render

from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import generics, status
from django.http import HttpResponse

from Backend.serializers import UsersSerializer

from Backend.models import User


class Authorization(APIView):

    def post(self, request):
        print(request.data)
        user_name = request.data.get('name')
        user = User.objects.get(name=user_name)
        return Response({"success": ":)"})
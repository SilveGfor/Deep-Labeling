from rest_framework import serializers
from Backend.models import User, Project


class UsersSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = "__all__"

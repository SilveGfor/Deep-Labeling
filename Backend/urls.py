from django.urls import path

from .views import Authorization

urlpatterns = [
    path('authorization', Authorization.as_view()),
]

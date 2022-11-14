from django.http import JsonResponse
from django.shortcuts import render
from rest_framework.generics import ListAPIView, RetrieveAPIView
from rest_framework.parsers import JSONParser
from rest_framework.views import APIView

from .serializer import *


class Registration(APIView):
    def post(self, request):
        data = JSONParser().parse(request)
        serializer = UserSerializer(data = data)
        if serializer.is_valid():
            user = serializer.save()
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.errors, status=400)

class Users(ListAPIView):
    serializer_class = UserSerializer
    model = serializer_class.Meta.model
    queryset = model.objects.all()
    paginate_by = 2

class UserDetails(RetrieveAPIView):
    lookup_field = "id"
    queryset = User.objects.all()
    serializer_class = UserSerializer

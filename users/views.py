from django.http import JsonResponse
from django.shortcuts import render
from rest_framework import permissions
from rest_framework.decorators import permission_classes
from rest_framework.generics import ListAPIView, RetrieveAPIView
from rest_framework.parsers import JSONParser
from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView

from question.models import Question
from question.serializers import QuestionSerializer

from .serializer import *


class Registration(APIView):
    def post(self, request):
        data = JSONParser().parse(request)
        serializer = UserSerializer(data = data)
        if serializer.is_valid():
            user = serializer.save()
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.errors, status=400)

class Sheikhs(ListAPIView):
    serializer_class = UserSerializer
    model = serializer_class.Meta.model
    queryset = model.objects.filter(is_sheikh=False)
    paginate_by = 2


class UserDetails(APIView):
    permission_classes = (IsAuthenticated, )
    def get(self, request):
        user = request.user
        serializer = UserSerializer(user)
        return JsonResponse(serializer.data, status=200)

class UserQuestions(ListAPIView):
    serializer_class = QuestionSerializer
    model = serializer_class.Meta.model
    
    def get_queryset(self):
        return Question.objects.filter(user__id=self.request.user.id)
    

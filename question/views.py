from django.http import JsonResponse
from rest_framework.generics import CreateAPIView, ListAPIView, RetrieveAPIView
from rest_framework.views import APIView

from .models import Question
from .serializers import QuestionAddSerializer, QuestionSerializer


class QuestionCreate(CreateAPIView):
    queryset = Question.objects.all()
    serializer_class = QuestionAddSerializer

class Questions(ListAPIView):
    serializer_class = QuestionSerializer
    model = serializer_class.Meta.model
    queryset = Question.objects.all()

class QuestionDetails(APIView):
    def get(self, reequest, id):
        question = Question.objects.get(id=id)
        question.views+=1
        question.save()
        serializer = QuestionSerializer(question)
        return JsonResponse(serializer.data)
    
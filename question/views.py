from rest_framework.generics import ListCreateAPIView

from .models import Question
from .serializers import QuestionSerializer

# class Registration(APIView):
#     def post(self, request):
#         data = JSONParser().parse(request)
#         serializer = UserSerializer(data = data)
#         if serializer.is_valid():
#             user = serializer.save()
#             return JsonResponse(serializer.data, status=201)
#         return JsonResponse(serializer.errors, status=400)

class Questions(ListCreateAPIView):
    serializer_class = QuestionSerializer
    model = serializer_class.Meta.model
    queryset = Question.objects.all()
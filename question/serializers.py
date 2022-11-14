from rest_framework import serializers

from users.models import User
from users.serializer import UserSerializer

from .models import Answer, Question


class QuestionSerializer(serializers.ModelSerializer):
    user = serializers.SerializerMethodField()
    class Meta:
        model = Question
        fields = "__all__"

    def get_user(self, obj):
        try:
            user_data = User.objects.get(id = obj.user.id)
            return  UserSerializer(user_data).data
        except:
            return {}
        
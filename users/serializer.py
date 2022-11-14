from rest_framework import serializers

from users.models import Profile, User


class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        exclude = ["id", "user"]

class UserSerializer(serializers.ModelSerializer):
    profile = serializers.SerializerMethodField()
    class Meta:
        model = User
        fields = ['id', 'first_name', 'last_name', 'email', 'is_sheikh', 'password', 'profile']
        extra_kwargs = {'password': {'write_only': True}}

    def get_profile(self, obj):
        try:
            get = Profile.objects.get(user__id = obj.id)
        except:
            get = {}
        return  ProfileSerializer(get).data

    def create(self, validated_data):
        user = User.objects.create_user(**validated_data)
        Profile.objects.create(user=user)
        return user
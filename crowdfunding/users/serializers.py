from rest_framework import serializers
from .models import CustomUser
from fundraisers.serializers import FundraiserSerializer, PledgeSerializer

class CustomUserSerializer(serializers.ModelSerializer):
    fundraisers = FundraiserSerializer(many=True, read_only=True, source='owned_fundraisers')
    pledges = PledgeSerializer(many=True, read_only=True)

    class Meta:
        model = CustomUser
        fields = ['username','email','password','fundraisers','pledges']
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        return CustomUser.objects.create_user(**validated_data)
    
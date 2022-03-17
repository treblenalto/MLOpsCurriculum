from rest_framework import serializers
from .models import User


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User  # select model
        fields = ("id", "name", "age")  # select fields
    
    def validate_name(self, instance):
        if instance.replace(" ", "").encode().isalpha()==False:
            raise serializers.ValidationError("Name must contain only alphabet letters")
        return instance.strip()
        
    def validate_age(self, instance):
        if instance < 0:
            raise serializers.ValidationError("Age must be positive")
        return instance
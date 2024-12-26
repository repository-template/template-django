from rest_framework import serializers

from .models import Animal  # Replace with your actual model name


class AnimalSerializer(serializers.ModelSerializer):
    class Meta:
        model = Animal  # Replace with your actual model name
        fields = (
            "__all__"  # Specify the fields you want to include in the serialization
        )

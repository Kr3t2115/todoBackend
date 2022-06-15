from rest_framework import serializers

from .models import todoModel

class todoSerializer(serializers.ModelSerializer):
    class Meta:
        model = todoModel
        fields = '__all__'
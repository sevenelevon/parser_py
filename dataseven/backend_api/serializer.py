from rest_framework import serializers
from .models import OneTest


class OneTestSerializer(serializers.ModelSerializer):
    class Meta:
        model = OneTest
        # Перечисляем поля в models чтобы преобразовать данные python обьекта в json
        fields = ['title', 'channel']

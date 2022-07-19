from rest_framework import serializers
from .models import Question, Alternative


class QuestionSerializers(serializers.ModelSerializer):
    class Meta:
        model = Question
        fields = '__all__'


class AlternativeSerializers(serializers.ModelSerializer):
    class Meta:
        model = Alternative
        fields = '__all__'
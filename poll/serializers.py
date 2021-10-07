from rest_framework import serializers


class QuestionSerializer(serializers.Serializer):
    id = serializers.IntegerField()
    title = serializers.CharField()
    pub_date = serializers.DateTimeField()
    end_date = serializers.DateTimeField()


class IdSerializer(serializers.Serializer):
    userId_id = serializers.IntegerField()

class AnswerSerializer(serializers.Serializer):
    userId = serializers.CharField()
    question = serializers.CharField()
    choice = serializers.CharField()
    created = serializers.DateTimeField()


class ChoicesSerializer(serializers.Serializer):
    id = serializers.IntegerField()
    question = serializers.CharField()
    title = serializers.CharField()
    lock_other = serializers.BooleanField()

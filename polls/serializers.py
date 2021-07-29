from . import models
from rest_framework import serializers


class PollsSerializer(serializers.HyperlinkedModelSerializer):
    url = serializers.HyperlinkedIdentityField(view_name="poll-detail")

    class Meta:
        model = models.Poll
        fields = ['url','id', 'name', 'start_date', 'end_date', 'description']

class QuestionSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = models.Question
        fields = ['id', 'url', 'text', 'type', 'poll']


class AnswerSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.Answer
        fields = ['url', 'id', 'answer', 'user','question' ]
        read_only_fields = ['user']

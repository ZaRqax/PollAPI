from rest_framework.authentication import SessionAuthentication, BasicAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import viewsets, permissions
from . import models
from .serializers import PollsSerializer, QuestionSerializer, AnswerSerializer
from django.contrib.auth import login


class PollsViewSet(viewsets.ModelViewSet):
    queryset = models.Poll.objects.filter(active=True)
    serializer_class = PollsSerializer
    permission_classes = [permissions.DjangoModelPermissionsOrAnonReadOnly]

    def update(self, request, pk=None, *args, **kwargs):
        data = request.data
        poll = models.Poll.objects.get(pk=pk)
        poll.name = data['name']
        poll.end_date = data['end_date']
        poll.description = data['description']
        poll.save()
        return Response(self.serializer_class(poll,context={'request': request}).data)


class QuestionViewSet(viewsets.ModelViewSet):
    queryset = models.Question.objects.filter(active=True)
    serializer_class = QuestionSerializer
    permission_classes = [permissions.DjangoModelPermissionsOrAnonReadOnly]


class AnswerViewSet(viewsets.ModelViewSet):
    serializer_class = AnswerSerializer
    permission_classes = [permissions.AllowAny]

    def create(self, request, *args, **kwargs):
        data = request.data
        user = request.user
        question = models.Question.objects.get(id=data['question'])
        answer = models.Answer(user=user, question=question, answer=data['answer'])
        answer.save()

    return Response(self.serializer_class(answer,context={'request': request}).data)

    def get_queryset(self):
        if not self.request.user.is_authenticated:
            u = models.User.objects.all()
            user = models.User(username=str(u[len(u) - 1].id + 1))
            user.save()
            login(request=self.request, user=user)
        queryset = models.Answer.objects.filter(user=self.request.user)
        return queryset


class MyAnswers(viewsets.ReadOnlyModelViewSet):
    serializer_class = AnswerSerializer
    permissions = [permissions.IsAuthenticated]
    queryset = models.Answer.objects.all()

    def list(self, request, *args, **kwargs):
        if not request.user.is_authenticated:
            return Response('Non authenticated')
        user = request.user
        answers = models.Answer.objects.filter(user=user)
        questions = models.Question.objects.filter(active=True)
        queryset = {}
        context = {'request': request}
        queryset['questions'] = QuestionSerializer(questions, context=context, many=True).data

        for question in questions:
            queryset[question.id] = (
                question.text, AnswerSerializer(answers.filter(question=question), many=True, context=context).data
            )

        return Response(queryset)

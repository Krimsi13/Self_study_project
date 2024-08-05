from django.shortcuts import render
from rest_framework.generics import CreateAPIView, ListAPIView, RetrieveAPIView, UpdateAPIView, DestroyAPIView

from knowledge_test.models import Test, Question, Answer

from knowledge_test.serializers import TestSerializer, QuestionSerializer, AnswerSerializer


class TestCreateApiView(CreateAPIView):
    """Create a new Test."""
    queryset = Test.objects.all()
    serializer_class = TestSerializer


class TestListApiView(ListAPIView):
    """List of Tests."""
    queryset = Test.objects.all()
    serializer_class = TestSerializer


class TestRetrieveApiView(RetrieveAPIView):
    """Get one Test."""
    queryset = Test.objects.all()
    serializer_class = TestSerializer


class TestUpdateApiView(UpdateAPIView):
    """Update Test."""
    queryset = Test.objects.all()
    serializer_class = TestSerializer


class TestDestroyApiView(DestroyAPIView):
    """Delete Test."""
    queryset = Test.objects.all()
    serializer_class = TestSerializer


class QuestionCreateApiView(CreateAPIView):
    """Create a new Question."""
    queryset = Question.objects.all()
    serializer_class = QuestionSerializer


class QuestionListApiView(ListAPIView):
    """List of Questions."""
    queryset = Question.objects.all()
    serializer_class = QuestionSerializer


class QuestionRetrieveApiView(RetrieveAPIView):
    """Get one Question."""
    queryset = Question.objects.all()
    serializer_class = QuestionSerializer


class QuestionUpdateApiView(UpdateAPIView):
    """Update Question."""
    queryset = Question.objects.all()
    serializer_class = QuestionSerializer


class QuestionDestroyApiView(DestroyAPIView):
    """Delete Question."""
    queryset = Question.objects.all()
    serializer_class = QuestionSerializer


class AnswerCreateApiView(CreateAPIView):
    """Create a new Answer."""
    queryset = Answer.objects.all()
    serializer_class = AnswerSerializer


class AnswerListApiView(ListAPIView):
    """List of Answer."""
    queryset = Answer.objects.all()
    serializer_class = AnswerSerializer


class AnswerRetrieveApiView(RetrieveAPIView):
    """Get one Answer."""
    queryset = Answer.objects.all()
    serializer_class = AnswerSerializer


class AnswerUpdateApiView(UpdateAPIView):
    """Update Answer."""
    queryset = Answer.objects.all()
    serializer_class = AnswerSerializer


class AnswerDestroyApiView(DestroyAPIView):
    """Delete Answer."""
    queryset = Answer.objects.all()
    serializer_class = AnswerSerializer

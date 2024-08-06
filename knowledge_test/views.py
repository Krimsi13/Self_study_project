from django.shortcuts import render
from rest_framework.generics import CreateAPIView, ListAPIView, RetrieveAPIView, UpdateAPIView, DestroyAPIView
from rest_framework.response import Response
from rest_framework.views import APIView

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


class CheckAnswerID(APIView):
    """Check answer by ID."""
    def post(self, request, *args, **kwargs):
        question_pk = kwargs["question_pk"]
        answer_pk = kwargs["answer_pk"]

        question = Question.objects.get(pk=question_pk)
        answers_list = question.answers.filter(is_correct=True).values()
        pk_list = []

        for answer in answers_list:
            pk_list.append(answer["id"])
        if answer_pk in pk_list:
            message = "Правильно!"
        else:
            message = "Неправильно!"

        return Response({"message": message})


class CheckAnswerText(APIView):
    """Check answer by Text."""
    def post(self, request, *args, **kwargs):
        question_pk = kwargs["question_pk"]
        answer_text = request.data.get('answer_text').lower()

        question = Question.objects.get(pk=question_pk)
        answers_list = question.answers.filter(is_correct=True).values()
        answers_list_text = []

        for answer in answers_list:
            answers_list_text.append(answer["answer_text"].lower())
        if answer_text in answers_list_text:
            message = "Правильно!"
        else:
            message = "Неправильно!"

        return Response({"message": message})

    # Вариант 1(id вопроса и текст ответа(неудачно))
    # def post(self, request, *args, **kwargs):
    #     question_pk = request.data.get('question_pk')
    #     answer_text = request.data.get('answer_text')
    #
    #     question = Question.objects.get(pk=question_pk)
    #     answer = Answer.objects.filter(question=question, text=answer_text).first()
    #
    #     if answer.is_correct:
    #         message = "Правильно!"
    #     else:
    #         message = "Неправильно!"
    #
    #     return Response({"message": message})



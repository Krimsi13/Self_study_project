from django.shortcuts import render
from rest_framework.generics import CreateAPIView, ListAPIView, RetrieveAPIView, UpdateAPIView, DestroyAPIView
from rest_framework.permissions import IsAdminUser, IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView

from knowledge_test.models import Test, Question, Answer

from knowledge_test.serializers import TestSerializer, QuestionSerializer, AnswerSerializer
from users.permissions import IsOwnerSection, IsOwner, IsOwnerTest, IsOwnerQuestion


class TestCreateApiView(CreateAPIView):
    """Create a new Test."""
    queryset = Test.objects.all()
    serializer_class = TestSerializer
    permission_classes = (IsAdminUser | IsOwnerSection,)


class TestListApiView(ListAPIView):
    """List of Tests."""
    queryset = Test.objects.all()
    serializer_class = TestSerializer
    permission_classes = (IsAuthenticated,)


class TestRetrieveApiView(RetrieveAPIView):
    """Get one Test."""
    queryset = Test.objects.all()
    serializer_class = TestSerializer
    permission_classes = (IsAuthenticated,)


class TestUpdateApiView(UpdateAPIView):
    """Update Test."""
    queryset = Test.objects.all()
    serializer_class = TestSerializer
    permission_classes = (IsAdminUser | IsOwnerSection,)


class TestDestroyApiView(DestroyAPIView):
    """Delete Test."""
    queryset = Test.objects.all()
    serializer_class = TestSerializer
    permission_classes = (IsAdminUser | IsOwnerSection,)


class QuestionCreateApiView(CreateAPIView):
    """Create a new Question."""
    queryset = Question.objects.all()
    serializer_class = QuestionSerializer
    permission_classes = (IsAdminUser | IsOwnerTest)


class QuestionListApiView(ListAPIView):
    """List of Questions."""
    queryset = Question.objects.all()
    serializer_class = QuestionSerializer
    permission_classes = (IsAuthenticated,)


class QuestionRetrieveApiView(RetrieveAPIView):
    """Get one Question."""
    queryset = Question.objects.all()
    serializer_class = QuestionSerializer
    permission_classes = (IsAuthenticated,)


class QuestionUpdateApiView(UpdateAPIView):
    """Update Question."""
    queryset = Question.objects.all()
    serializer_class = QuestionSerializer
    permission_classes = (IsAdminUser | IsOwnerTest,)


class QuestionDestroyApiView(DestroyAPIView):
    """Delete Question."""
    queryset = Question.objects.all()
    serializer_class = QuestionSerializer
    permission_classes = (IsAdminUser | IsOwnerTest,)


class AnswerCreateApiView(CreateAPIView):
    """Create a new Answer."""
    queryset = Answer.objects.all()
    serializer_class = AnswerSerializer
    permission_classes = (IsAdminUser | IsOwnerQuestion,)


class AnswerListApiView(ListAPIView):
    """List of Answer."""
    queryset = Answer.objects.all()
    serializer_class = AnswerSerializer
    permission_classes = (IsAuthenticated,)


class AnswerRetrieveApiView(RetrieveAPIView):
    """Get one Answer."""
    queryset = Answer.objects.all()
    serializer_class = AnswerSerializer
    permission_classes = (IsAuthenticated,)


class AnswerUpdateApiView(UpdateAPIView):
    """Update Answer."""
    queryset = Answer.objects.all()
    serializer_class = AnswerSerializer
    permission_classes = (IsAdminUser | IsOwnerQuestion,)


class AnswerDestroyApiView(DestroyAPIView):
    """Delete Answer."""
    queryset = Answer.objects.all()
    serializer_class = AnswerSerializer
    permission_classes = (IsAdminUser | IsOwnerQuestion,)


class CheckAnswerID(APIView):
    """Check answer by ID."""
    permission_classes = (IsAuthenticated,)

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
    permission_classes = (IsAuthenticated,)

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


class QuestionListOfTest(APIView):
    """Get List of Questions by ID Test."""
    permission_classes = (IsAuthenticated,)

    def get(self, request, *args, **kwargs):
        test_pk = kwargs["test_pk"]
        questions_list = Question.objects.filter(test=test_pk).values()

        return Response(questions_list)


class AnswerListOfQuestion(APIView):
    """Get List of Answers by ID Question."""
    permission_classes = (IsAuthenticated,)

    def get(self, request, *args, **kwargs):
        question_pk = kwargs["question_pk"]
        answers_list = Answer.objects.filter(question=question_pk).values()

        return Response(answers_list)

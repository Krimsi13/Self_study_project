from django.urls import path

from knowledge_test.apps import KnowledgeTestConfig
from knowledge_test.views import (TestListApiView, TestRetrieveApiView, TestCreateApiView, TestUpdateApiView,
                                  TestDestroyApiView, QuestionListApiView, QuestionRetrieveApiView,
                                  QuestionCreateApiView, QuestionUpdateApiView, QuestionDestroyApiView,
                                  AnswerListApiView, AnswerRetrieveApiView, AnswerCreateApiView, AnswerUpdateApiView,
                                  AnswerDestroyApiView)

app_name = KnowledgeTestConfig.name

urlpatterns = [
    # CRUD Test
    path("", TestListApiView.as_view(), name="tests_list"),
    path("<int:pk>/", TestRetrieveApiView.as_view(), name="tests_retrieve"),
    path("create/", TestCreateApiView.as_view(), name="tests_create"),
    path("<int:pk>/update/", TestUpdateApiView.as_view(), name="tests_update"),
    path("<int:pk>/delete/", TestDestroyApiView.as_view(), name="tests_delete"),

    # CRUD Question
    path("questions/", QuestionListApiView.as_view(), name="questions_list"),
    path("questions/<int:pk>/", QuestionRetrieveApiView.as_view(), name="questions_retrieve"),
    path("questions/create/", QuestionCreateApiView.as_view(), name="questions_create"),
    path("questions/<int:pk>/update/", QuestionUpdateApiView.as_view(), name="questions_update"),
    path("questions/<int:pk>/delete/", QuestionDestroyApiView.as_view(), name="questions_delete"),

    # CRUD Answer
    path("answers/", AnswerListApiView.as_view(), name="answers_list"),
    path("answers/<int:pk>/", AnswerRetrieveApiView.as_view(), name="answers_retrieve"),
    path("answers/create/", AnswerCreateApiView.as_view(), name="answers_create"),
    path("answers/<int:pk>/update/", AnswerUpdateApiView.as_view(), name="answers_update"),
    path("answers/<int:pk>/delete/", AnswerDestroyApiView.as_view(), name="answers_delete"),
]

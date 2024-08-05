from django.db import models

from config import settings
from education.models import Section

NULLABLE = {"null": True, "blank": True}


class Test(models.Model):
    title = models.CharField(max_length=255, verbose_name="Название теста")
    section = models.ForeignKey(Section, on_delete=models.CASCADE, verbose_name="Раздел", **NULLABLE)

    class Meta:
        verbose_name = "Тест"
        verbose_name_plural = "Тесты"

    def __str__(self):
        return self.title


class Question(models.Model):
    question_number = models.PositiveIntegerField(verbose_name="Номер вопроса", **NULLABLE)
    question_text = models.TextField(verbose_name="Текст вопроса")
    test = models.ForeignKey(Test, on_delete=models.CASCADE, verbose_name="Тест", related_name="questions", **NULLABLE)

    class Meta:
        verbose_name = "Вопрос"
        verbose_name_plural = "Вопросы"

    def __str__(self):
        return self.question_number


class Answer(models.Model):
    answer_number = models.PositiveIntegerField(verbose_name="Номер ответа", **NULLABLE)
    answer_text = models.CharField(max_length=255, verbose_name="Текст ответа")
    is_correct = models.BooleanField(default=False, verbose_name="Признак правильного ответа")
    question = models.ForeignKey(Question, on_delete=models.CASCADE, verbose_name="Вопрос", related_name="answers",
                                 **NULLABLE)

    class Meta:
        verbose_name = "Ответ"
        verbose_name_plural = "Ответы"

    def __str__(self):
        return self.answer_number

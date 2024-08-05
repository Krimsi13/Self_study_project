from django.db import models

from config import settings

NULLABLE = {"null": True, "blank": True}


class Section(models.Model):
    title = models.CharField(max_length=255, verbose_name="Название раздела")
    preview = models.ImageField(
        upload_to="education/preview/", **NULLABLE, verbose_name="Картинка"
    )
    description = models.TextField(verbose_name="Описание раздела")

    owner = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, **NULLABLE, verbose_name="Владелец",
                              help_text="Укажите владельца раздела(курса)")

    class Meta:
        verbose_name = "Раздел"
        verbose_name_plural = "Раздел"

    def __str__(self):
        return self.title


class Material(models.Model):
    title = models.CharField(max_length=255, verbose_name="Название материала(урока)")
    description = models.TextField(verbose_name="Описание материала(урока)")
    preview = models.ImageField(
        upload_to="materials/preview/", **NULLABLE, verbose_name="Картинка"
    )
    link_to_video = models.URLField(verbose_name="Ссылка на видео", **NULLABLE)

    section = models.ForeignKey(
        Section, on_delete=models.CASCADE, related_name="materials", verbose_name="Раздел", **NULLABLE
    )

    owner = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, **NULLABLE, verbose_name="Владелец",
                              help_text="Укажите владельца материала(урока)")

    class Meta:
        verbose_name = "Материал"
        verbose_name_plural = "Материалы"

    def __str__(self):
        return self.title

from django.contrib.auth import get_user_model
from django.db import models

User = get_user_model()


class Post(models.Model):
    title = models.CharField(max_length=300, blank=True, null=True, verbose_name='Заголовок')
    content = models.TextField(verbose_name='Содержание', null=True)
    published = models.DateTimeField(auto_now_add=True, db_index=True, verbose_name='Время публикации')
    rubric = models.ForeignKey(
        'Rubric',
        null=True,
        on_delete=models.PROTECT,
        verbose_name='Рубрика',
        related_name='post',
    )
    author = models.ForeignKey(
        User,
        on_delete=models.SET_DEFAULT,
        default='',
        null=False,
        verbose_name='Пользователь',
        related_name='post'
    )


class Rubric(models.Model):
    name = models.CharField(max_length=20, db_index=True, verbose_name='Название')

    class Meta:
        verbose_name_plural = 'Рубрики'
        verbose_name = 'Рубрика'
        ordering = ['name']

    def __str__(self):
        return self.name
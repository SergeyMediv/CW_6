from django.db import models

NULLABLE = {'null': 'True', 'blank': 'True'}


class Blog(models.Model):
    title = models.CharField(max_length=100, verbose_name='Заголовок')
    content = models.TextField(verbose_name='Содержимое')
    image = models.ImageField(upload_to='products/', verbose_name='Превью', **NULLABLE)
    created_at = models.DateField(verbose_name='Дата создания', auto_now_add=True)
    is_published = models.BooleanField(verbose_name='Опубликовано', default=True)
    views_count = models.PositiveSmallIntegerField(verbose_name='Просмотры', default=0)

    class Meta:
        verbose_name = 'Статья'
        verbose_name_plural = 'Статьи'
        ordering = ('created_at',)

from django.db import models

class Tag(models.Model):
    name = models.CharField(max_length=100, unique=True)

    class Meta:
        verbose_name = 'Раздел'
        verbose_name_plural = 'Разделы'
        ordering = ['name']

    def __str__(self):
        return self.name

class Scope(models.Model):
    article = models.ForeignKey(
        'Article',
        on_delete=models.CASCADE,
        related_name='scopes'
    )

    tag = models.ForeignKey(
        'Tag',
        on_delete=models.CASCADE,
        related_name='scopes'
    )
    is_main = models.BooleanField(default=False)

    class Meta:
        verbose_name = 'Связь статьи и раздела'
        verbose_name_plural = 'Связи статей и разделов'
        unique_together = ('article', 'tag')
        ordering = ['-is_main', 'tag__name']

class Article(models.Model):

    title = models.CharField(max_length=256, verbose_name='Название')
    text = models.TextField(verbose_name='Текст')
    published_at = models.DateTimeField(verbose_name='Дата публикации')
    image = models.ImageField(null=True, blank=True, verbose_name='Изображение',)

    tags = models.ManyToManyField(
        'Tag',
        through='Scope',
        related_name='articles'
    )

    class Meta:
        verbose_name = 'Статья'
        verbose_name_plural = 'Статьи'
        ordering = ['-published_at']

    def __str__(self):
        return self.title
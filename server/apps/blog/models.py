from django.db import models

from apps.users.models.profiles import Profile


class Tag(models.Model):
    name = models.CharField('Название', max_length=90)

    class Meta:
        verbose_name = 'Тэг'
        verbose_name_plural = 'Тэги'

    def __str__(self):
        return f'{self.name}'


class Post(models.Model):
    author = models.ForeignKey(Profile, verbose_name='Автор', on_delete=models.PROTECT)
    title = models.CharField('Заголовок', max_length=120)
    tags = models.ManyToManyField(Tag, verbose_name='Тэги', on_delete=models.CASCADE, related_name='posts')
    text = models.TextField('Текст')
    created = models.DateTimeField('Создано', auto_now_add=True)
    last_modified = models.DateTimeField('Последнее изменение', auto_now=True)

    class Meta:
        verbose_name = 'Пост'
        verbose_name_plural = 'Посты'

    def __str__(self):
        return f'Пост {self.title} от {self.created}'


class PostComment(models.Model):
    post = models.ForeignKey(Post, verbose_name='Пост', on_delete=models.CASCADE, related_name='post_comment')
    author = models.ForeignKey(Profile, verbose_name='Автор', on_delete=models.CASCADE, related_name='post_comments')
    text = models.TextField('Текст')
    created = models.DateTimeField('Создано', auto_now_add=True)
    last_modified = models.DateTimeField('Последнее изменение', auto_now=True)

    class Meta:
        verbose_name = 'Комментарий к посту'
        verbose_name_plural = 'Коментарии к посту'

    def __str__(self):
        return f'Комментарий от {self.author} к {self.post.title}'


class MinorPostComment(models.Model):
    comment = models.ForeignKey(Post, verbose_name='Главный комментарий', on_delete=models.CASCADE, related_name='minor_comment')
    author = models.ForeignKey(Profile, verbose_name='Автор', on_delete=models.CASCADE)
    text = models.TextField('Текст')
    created = models.DateTimeField('Создано', auto_now_add=True)
    last_modified = models.DateTimeField('Последнее изменение', auto_now=True)

    class Meta:
        verbose_name = 'Ответ на коментарий'
        verbose_name_plural = 'Ответы на коментарии'

    def __str__(self):
        return f'Ответ к {self.comment} к {self.post.title}'

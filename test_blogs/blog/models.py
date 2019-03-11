from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User

# Create your models here.

class Article(models.Model):
    user_id = models.ForeignKey(User, on_delete=models.CASCADE) # Багато статей може написати 1 автор

    title = models.CharField(max_length = 30, verbose_name = 'Заголовок')
    img = models.ImageField('Картинка', upload_to = 'blog/photos', blank = True)
    body = models.TextField(verbose_name='Тело статьи')


    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('article_detail', args=[str(self.id)])


class Comment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE) # Багато коментарів може написати юзер
    article_id = models.ForeignKey(Article, on_delete=models.CASCADE) # Багато коментарів може мати статья

    contentx = models.TextField()
    date = models.DateTimeField(auto_now_add=True, verbose_name = 'Дата')

    def get_absolute_url(self):
        return reverse('article_detail', args=[str(self.article_id.id)])

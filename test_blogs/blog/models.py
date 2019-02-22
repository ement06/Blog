from django.db import models

# Create your models here.

class Article(models.Model):
    title = models.CharField(max_length = 30, verbose_name = 'Заголовок')
    img = models.ImageField('Картинка', upload_to = 'blog/photos', blank = True)
    body = models.TextField(verbose_name='Тело статьи')

    def __str__(self):
        return self.title


class Create_post(models.Model):
    article = models.ForeignKey(Article, on_delete=models.CASCADE, verbose_name = 'Статья')
    # comentar = models
    autor = models.CharField(max_length = 10, verbose_name = 'Ник автора')
    email = models.EmailField(max_length = 30, verbose_name = 'Контакт автора')
    date = models.DateTimeField(auto_now_add=True, verbose_name = 'Дата')

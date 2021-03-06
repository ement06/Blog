from django.urls import path
from .views import *


urlpatterns = [
    path('', ArticleList.as_view(), name='article_list'),
    path('view/<int:pk>', ArticleDetail.as_view(), name='article_detail'),
    path('create/', ArticleCreate.as_view(), name='article_new'),
    path('comment/add', CommentCreate.as_view(), name = 'comment_new'),
    path('edit/<int:pk>', ArticleUpdate.as_view(), name='article_edit'),
    path('delete/<int:pk>', ArticleDelete.as_view(), name='article_delete')
]

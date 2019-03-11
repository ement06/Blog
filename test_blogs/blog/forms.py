from django import forms
from blog.models import Article, Comment


# class ArticleForm(forms.ModelForm):
#     class Meta:
#         model = Article
#         fields = ('title', 'img', 'body')
#
#
# class CreatePostFrom(forms.ModelForm):
#     class Meta:
#         model = Create_post
#         fields = ('article', 'autor', 'email')

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('article_id','user', 'contentx')
        widgets = {'article_id': forms.HiddenInput(), 'user': forms.HiddenInput()}

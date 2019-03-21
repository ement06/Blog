from django import forms
from blog.models import Article, Comment
from django.contrib.auth.models import User

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('article_id','user', 'contentx')
        widgets = {'article_id': forms.HiddenInput(), 'user': forms.HiddenInput()}


class RegisterUserFrom(forms.ModelForm):
    password1 = forms.CharField(label = 'Пароль', widget = forms.PasswordInput)
    password2 = forms.CharField(label = 'Повторіть пароль', widget = forms.PasswordInput)


    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name')

        def clean_password2(self):
            cd = self.cleaned_data
            if cd[password1] != cd[password2]:
                raise forms.ValidationError('Не правильно введений пароль')
            return cd[password2]

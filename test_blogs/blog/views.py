from django.shortcuts import render, get_object_or_404, redirect
from blog.models import Article, Comment

from blog.forms import CommentForm, RegisterUserFrom

from django.http import HttpResponseRedirect
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView, FormView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import BaseUserManager
from django.contrib.auth import login, authenticate

# Create your views here.

def register(request):
    if request.method == "POST":
        user_form = RegisterUserFrom(request.POST)

        if user_form.is_valid():
            new_user = user_form.save(commit=False)
            new_user.set_password(user_form.cleaned_data['password2'])
            new_user.is_staff = True
            new_user.save()
            new_user = authenticate(username=user_form.cleaned_data['username'],
                                    password=user_form.cleaned_data['password2'],)
            login(request, new_user)
            return redirect('/blog/')
    else:
        user_form = RegisterUserFrom()

    return render(request, 'register.html', {'form': user_form})


class ArticleList(ListView):
    model = Article

class ArticleDetail(DetailView):
    model = Article

    def get_context_data(self, **kwargs):
        context = super(ArticleDetail, self).get_context_data(**kwargs)
        context['comment'] = Comment.objects.filter(article_id = self.kwargs['pk'])
        context['comment_add'] = CommentForm(initial={'article_id': self.kwargs['pk'], 'user': self.request.user})
        return context


class ArticleCreate(LoginRequiredMixin, CreateView):
    model = Article
    def form_valid(self, form):
        form.instance.user_id = self.request.user
        return super().form_valid(form)

    fields = ['title', 'img', 'body']
    login_url = '/log-in/'

class CommentCreate(CreateView):
    model = Comment
    form_class = CommentForm
    http_method_names = ['post']
    template_name = 'blog/comment_form.html'


class ArticleUpdate(LoginRequiredMixin, UpdateView):
    model = Article
    fields = ['title', 'img', 'body']
    login_url = '/log-in/'

class ArticleDelete(LoginRequiredMixin, DeleteView):
    model = Article
    success_url = reverse_lazy('article_list')
    login_url = '/log-in/'

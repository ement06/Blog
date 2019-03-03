from django.shortcuts import render, get_object_or_404
from blog.models import Article, Comment

# from blog.forms import CreatePostFrom, ArticleForm

from django.http import HttpResponseRedirect
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin

# Create your views here.
class ArticleList(ListView):
    model = Article

# def main_page(request):
#     articles = Article.objects.all()
#
#     return render(request, 'base.html', {
#         'articles': articles
#     })

class ArticleDetail(DetailView):
    model = Article

    def get_context_data(self, **kwargs):
        context = super(ArticleDetail, self).get_context_data(**kwargs)
        context['comment'] = Comment.objects.all()
        return context

# def article_detail(request, article_id):
#     article = get_object_or_404(Article, id = article_id)
#     return render(request, 'article_detail.html', {'item': article})

class ArticleCreate(LoginRequiredMixin, CreateView):
    model = Article
    fields = ['title', 'img', 'body']
    success_url = reverse_lazy('article_list')
    login_url = '/log-in/'

# def create_blog(request):
#
#     if request.method == "POST":
#         form = ArticleForm(request.POST, request.FILES)
#         if form.is_valid():
#             form.save()
#             return HttpResponseRedirect(reverse('main_page'))
#     else:
#         form = ArticleForm()
#
#     return render(request, 'create_blog.html', {
#         'form': form })

class ArticleUpdate(LoginRequiredMixin, UpdateView):
    model = Article
    fields = ['title', 'img', 'body']
    success_url = reverse_lazy('article_list')
    login_url = '/log-in/'

class ArticleDelete(LoginRequiredMixin, DeleteView):
    model = Article
    success_url = reverse_lazy('article_list')
    login_url = '/log-in/'

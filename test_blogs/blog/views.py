from django.shortcuts import render, get_object_or_404
from blog.models import Article

# from blog.forms import CreatePostFrom, ArticleForm

from django.http import HttpResponseRedirect
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView

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

# def article_detail(request, article_id):
#     article = get_object_or_404(Article, id = article_id)
#     return render(request, 'article_detail.html', {'item': article})

class ArticleCreate(CreateView):
    model = Article
    fields = ['title', 'img', 'body']
    success_url = reverse_lazy('article_list')

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

class ArticleUpdate(UpdateView):
    model = Article
    fields = ['title', 'img', 'body']
    success_url = reverse_lazy('article_list')

class ArticleDelete(DeleteView):
    model = Article
    success_url = reverse_lazy('article_list')

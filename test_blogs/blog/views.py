from django.shortcuts import render, get_object_or_404
from blog.models import Article, Comment

from blog.forms import CommentForm

from django.http import HttpResponseRedirect
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin

# Create your views here.
def func_request(request):
    body_data = request.session
    print(body_data)

    return render(request, 'some.html')

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

        print(self.kwargs['pk'])

        context['comment'] = Comment.objects.filter(article_id = self.kwargs['pk'])
        context['comment_add'] = CommentForm(initial={'article_id': self.kwargs['pk'], 'user': self.request.user})
        return context

# def article_detail(request, article_id):
#     article = get_object_or_404(Article, id = article_id)
#     return render(request, 'article_detail.html', {'item': article})

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
    login_url = '/log-in/'

class ArticleDelete(LoginRequiredMixin, DeleteView):
    model = Article
    success_url = reverse_lazy('article_list')
    login_url = '/log-in/'

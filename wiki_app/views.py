from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.db.models import Q
from .models import Article, Category

# defines the model for viewing available articles
class ArticleListView(ListView):
    model = Article
    template_name = 'wiki_app/article_list.html'
    context_object_name = 'articles'
    paginate_by = 10

    # retrieves relevant information for an article
    def get_queryset(self):
        query = self.request.GET.get('q')
        if query:
            return Article.objects.filter(
                Q(title__icontains=query) |
                Q(content__icontains=query) |
                Q(tags__icontains=query)
            )
        return super().get_queryset()

# defines model for detailed view of an article, 
# entering a article.
class ArticleDetailView(DetailView):
    model = Article
    template_name = 'wiki_app/article_detail.html'
    slug_field = 'slug'
    slug_url_kwarg = 'slug'

# view for creating an article, user decides
# title, content, category as well as tags.
class ArticleCreateView(LoginRequiredMixin, CreateView):
    model = Article
    fields = ['title', 'content', 'category', 'tags']
    template_name = 'wiki_app/article_form.html'

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

# view for updating an existing article.
class ArticleUpdateView(LoginRequiredMixin, UpdateView):
    model = Article
    fields = ['title', 'content', 'category', 'tags']
    template_name = 'wiki_app/article_form.html'
    slug_field = 'slug'
    slug_url_kwarg = 'slug'

# view for deleting an existing article.
class ArticleDeleteView(LoginRequiredMixin, DeleteView):
    model = Article
    template_name = 'wiki_app/article_confirm_delete.html'
    success_url = '/'
    slug_field = 'slug'
    slug_url_kwarg = 'slug'
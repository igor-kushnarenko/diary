from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView, TemplateView

from book.models import Post, Rubric
from book.forms import PostForm


def index_view(request):
    posts = Post.objects.all()
    rubrics = Rubric.objects.all()
    count = Post.objects.count()
    context = {'posts': posts, 'rubrics': rubrics, 'count': count}
    return render(request, 'book/index.html', context)


def by_rubric_view(request, rubric_id):
    posts = Post.objects.filter(rubric=rubric_id)
    rubrics = Rubric.objects.all()
    current_rubric = Rubric.objects.get(pk=rubric_id)
    context = {'posts': posts, 'rubrics': rubrics, 'current_rubric': current_rubric}
    return render(request, 'book/by_rubric.html', context)


class PostCreateView(CreateView):
    template_name = 'book/create.html'
    success_url = reverse_lazy('index')
    form_class = PostForm

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['posts'] = Post.objects.all()
        return context


class TestView(TemplateView):
    template_name = 'book/test.html'

    def get_context_data(self, **kwargs):
        context = super(TestView, self).get_context_data(**kwargs)
        context['rubrics'] = Rubric.objects.all()
        context['latest'] = Post.objects.all()[:5]
        context['count'] = Post.objects.count()
        return context

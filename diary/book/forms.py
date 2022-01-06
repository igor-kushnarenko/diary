from django.forms import ModelForm

from book.models import Post, Rubric


class PostForm(ModelForm):
    class Meta:
        model = Post
        fields = ('title', 'content', 'rubric', 'author')


class RubricForm(ModelForm):
    class Meta:
        model = Rubric
        fields = ['name']
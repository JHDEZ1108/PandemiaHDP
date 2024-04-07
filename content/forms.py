from django import forms
from django.forms import ModelForm
from .models import Comment, Blog

class CommentForm(ModelForm):
    class Meta:
        model = Comment
        fields = ['content']
        widgets = {
            'content': forms.Textarea(attrs={'placeholder': 'Agregar comentario...'}),
        }

class BlogForm(ModelForm):
    class Meta:
        model = Blog
        fields = ['title', 'subtitle', 'content', 'content2']

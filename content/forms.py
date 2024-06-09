from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Comment, Blog, Disease, DiseaseComment

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['content']
        widgets = {
            'content': forms.Textarea(attrs={'placeholder': 'Agregar comentario...'}),
        }

class BlogForm(forms.ModelForm):
    class Meta:
        model = Blog
        fields = ['title', 'subtitle', 'content', 'content2']
        
class DiseaseCommentForm(forms.ModelForm):
    class Meta:
        model = DiseaseComment
        fields = ['content']
        widgets = {
            'content': forms.Textarea(attrs={'placeholder': 'Agregar comentario...'}),
        }
                
class DiseaseForm(forms.ModelForm):
    class Meta:
        model = Disease
        fields = ['name', 'image', 'description']
                
class SignUpForm(UserCreationForm):
    first_name = forms.CharField(max_length=100, required=True, widget=forms.TextInput(attrs={'placeholder': 'Nombre'}))
    last_name = forms.CharField(max_length=100, required=True, widget=forms.TextInput(attrs={'placeholder': 'Apellido'}))
    
    class Meta(UserCreationForm.Meta):
        model = User
        fields = UserCreationForm.Meta.fields + ('first_name', 'last_name')

    def save(self, commit=True):
        user = super().save(commit=False)
        user.first_name = self.cleaned_data["first_name"]
        user.last_name = self.cleaned_data["last_name"]
        if commit:
            user.save()
        return user

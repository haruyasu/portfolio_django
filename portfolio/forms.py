from django import forms
from portfolio.models import Post, Comment

class PostForm(forms.ModelForm):

    class Meta():
        model = Post
        fields = ('author', 'title', 'text', 'image_list', 'client', 'date', 'skills', 'demo')

        widgets = {
            'title': forms.TextInput(attrs={'class': 'textinputclass'}),
            'text': forms.Textarea(attrs={'class': 'editable medium-editor-textarea postcontent'}),
            'client': forms.TextInput(attrs={'class': 'textinputclass'}),
            'date': forms.TextInput(attrs={'class': 'textinputclass'}),
            'skills': forms.TextInput(attrs={'class': 'textinputclass'}),
            'demo': forms.TextInput(attrs={'class': 'textinputclass'}),
        }

class CommentForm(forms.ModelForm):

    class Meta():
        model = Comment
        fields = ('author', 'text')

        widgets = {
            'author': forms.TextInput(attrs={'class': 'textinputclass'}),
            'text': forms.Textarea(attrs={'class': 'editable medium-editor-textarea'}),
        }
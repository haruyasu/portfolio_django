from django import forms
from portfolio.models import Post, Comment

class PostForm(forms.ModelForm):

    class Meta():
        model = Post
        fields = ('title', 'text', 'category', 'thumbnail', 'image_list', 'video', 'client', 'date', 'skills', 'demo')

        widgets = {
            'title': forms.TextInput(attrs={'class': 'textinput'}),
            'text': forms.Textarea(attrs={'class': 'descinput editable medium-editor-textarea postcontent'}),
            'category': forms.TextInput(attrs={'class': 'textinput'}),
            'thumbnail': forms.TextInput(attrs={'class': 'textinput'}),
            'image_list': forms.TextInput(attrs={'class': 'textinput'}),
            'video': forms.TextInput(attrs={'class': 'textinput'}),
            'client': forms.TextInput(attrs={'class': 'textinput'}),
            'date': forms.TextInput(attrs={'class': 'textinput'}),
            'skills': forms.TextInput(attrs={'class': 'textinput'}),
            'demo': forms.TextInput(attrs={'class': 'textinput'}),
        }

class CommentForm(forms.ModelForm):

    class Meta():
        model = Comment
        fields = ('author', 'text')

        widgets = {
            'author': forms.TextInput(attrs={'class': 'selectinput'}),
            'text': forms.Textarea(attrs={'class': 'descinput editable medium-editor-textarea'}),
        }
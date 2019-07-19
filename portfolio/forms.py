from django import forms
from portfolio.models import Post, Comment
from django.conf import settings
from django.core.mail import BadHeaderError, send_mail
from django.http import HttpResponse

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

class ContactForm(forms.Form):
    name = forms.CharField(
        label='',
        max_length=100,
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': "Name*",
        }),
    )
    email = forms.EmailField(
        label='',
        widget=forms.EmailInput(attrs={
            'class': 'form-control',
            'placeholder': "Email*",
        }),
    )
    message = forms.CharField(
        label='',
        widget=forms.Textarea(attrs={
            'class': 'form-control',
            'placeholder': "Message*",
        }),
    )

    def send_email(self):
        subject = "Contact from Portfolio"
        message = self.cleaned_data['message']
        name = self.cleaned_data['name']
        email = self.cleaned_data['email']
        from_email = '{name} <{email}>'.format(name=name, email=email)
        recipient_list = [settings.EMAIL_HOST_USER]
        try:
            send_mail(subject, message, from_email, recipient_list)
        except BadHeaderError:
            return HttpResponse("無効なヘッダが検出されました。")

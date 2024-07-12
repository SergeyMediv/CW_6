from django import forms

from blog.models import Blog
from mailing.forms import forbidden_words, StyleFormMixin


class BlogForm(StyleFormMixin, forms.ModelForm):
    class Meta:
        model = Blog
        fields = ['title', 'content', 'image']

    def clean_title(self):
        cleaned_data = self.cleaned_data['name']
        for word in forbidden_words:
            if word.lower() in cleaned_data.lower():
                raise forms.ValidationError('Заголовок не должен содержать запрещённых слов')
            else:
                return cleaned_data

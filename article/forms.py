from django import forms
from .models import Article

class ArticleForm(forms.ModelForm): #그냥 폼이랑 다름
    class Meta:
        model = Article
        fields = [
            'title',
            'content',
        ]
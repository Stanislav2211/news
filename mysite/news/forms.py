from .models import Articles
from django.forms import ModelForm, TextInput, DateTimeInput, Textarea


class ArticlesForm(ModelForm):
    class Meta:
        model = Articles
        fields = ['title', 'anons', 'full_text', 'date']
        widgets = {
            'title': TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Назва Статті'
            }),
            "anons": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Анонс Статті'
            }),
            "date": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Дата Публікації'
            }),
            "full_text": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Текст Статті',
            })
        }

from django import forms
from .models import News
from django.core.files.uploadedfile import SimpleUploadedFile

class NewsForm(forms.ModelForm):
    class Meta:
        model = News
        # fields = '__all__'
        fields = ['title', 'content', 'photo', 'is_published', 'category' ]
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'content': forms.Textarea(attrs={'class': 'form-control', 'rows': 5}),
            'category': forms.Select(attrs={'class': 'form-control'}),
        }
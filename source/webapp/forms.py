from django import forms
from .models import Status,Type

BROWSER_DATETIME_FORMAT = '%Y-%m-%dT%H:%M'

class ArticleForm(forms.Form):
    description = forms.CharField(max_length=200, required=True, label='Описание')
    maxdescription = forms.CharField(max_length=3000, required=True, label='Подробное описание', widget=forms.Textarea)
    status = forms.ModelChoiceField(queryset=Status.objects.all(),  label='Статус')
    type = forms.ModelChoiceField(queryset=Type.objects.all(), label='Тип')
    publish_at = forms.DateTimeField(required=False, label='Время публикации',
                                     input_formats=['%Y-%m-%d', BROWSER_DATETIME_FORMAT,
                                                    '%Y-%m-%dT%H:%M:%S', '%Y-%m-%d %H:%M',
                                                    '%Y-%m-%d %H:%M:%S'],
                                     widget=forms.DateTimeInput(attrs={'type': 'datetime-local'}))
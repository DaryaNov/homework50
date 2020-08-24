from django import forms
from .models import Article, Status,Type,Project
from django.core.exceptions import ValidationError
from django.core.validators import validate_slug



BROWSER_DATETIME_FORMAT = '%Y-%m-%dT%H:%M'


def at_least_5(string):
    if len(string) < 5:
        raise ValidationError('This value is too short!')



def desc(string):
    try:
        validate_slug(string)
    except ValidationError:
        print("invalid input passed to validate_slug()")



def word(words):
    if words.find('secret') != -1:
        raise ValidationError("You cannot enter the word secret!")




class ArticleForm(forms.ModelForm):
    project = forms.ModelMultipleChoiceField(queryset=Project.objects.all(), required=False, label='Проект')
    description = forms.CharField(max_length=200, required=True, label='Описание',validators=(at_least_5,))
    maxdescription = forms.CharField(max_length=3000, required=True, label='Подробное описание', widget=forms.Textarea,validators=(desc,word,))
    status = forms.ModelChoiceField(queryset=Status.objects.all(),  label='Статус')
    types = forms.ModelMultipleChoiceField(queryset=Type.objects.all(), required=False,label='Тип')
    publish_at = forms.DateTimeField(required=False, label='Время публикации',
                                     input_formats=['%Y-%m-%d', BROWSER_DATETIME_FORMAT,
                                                    '%Y-%m-%dT%H:%M:%S', '%Y-%m-%d %H:%M',
                                                    '%Y-%m-%d %H:%M:%S'],
                                     widget=forms.DateTimeInput(attrs={'type': 'datetime-local'}))



    class Meta:
        model = Article
        fields = ['description', 'maxdescription', 'status', 'types','publish_at']


class SimpleSearchForm(forms.Form):
    search = forms.CharField(max_length=100, required=False, label="Найти")



class ArticleProjectForm(forms.ModelForm):
    class Meta:
        model = Project
        fields = ['name', 'text' ,'newdate_at','enddate_at']
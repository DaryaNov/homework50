from django.db import models
from django.utils import timezone
from django.core.validators import MinLengthValidator


class Article(models.Model):

    description = models.CharField(max_length=2000, null=False, blank=False, verbose_name='Описание',validators=[MinLengthValidator(5)])
    maxdescription = models.TextField(max_length=2000,null=True,blank=False,verbose_name='Подробное описание')
    types = models.ManyToManyField('webapp.Type',related_name='type_key', blank=True, verbose_name='Тип')
    status = models.ForeignKey('Status',related_name='status_key',on_delete=models.CASCADE, verbose_name='Статус')
    publish_at = models.DateTimeField(verbose_name="Время публикации", blank=True, default=timezone.now)
    updated_at = models.DateTimeField(verbose_name='Время изменения', blank=True, default=timezone.now)


    def __str__(self):
        return "{}. {}".format(self.pk, self.description)


    class Meta:
        verbose_name = 'Задача'
        verbose_name_plural = 'Задачи'



class Type(models.Model):
    name = models.CharField(max_length = 30, default = 'task', verbose_name = 'Тип')


    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Тип'
        verbose_name_plural = 'Типы'


class Status(models.Model):
    name = models.CharField(max_length=30, default='new',verbose_name='Статус')


    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Статус'
        verbose_name_plural = 'Статусы'
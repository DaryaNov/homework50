from django.conf import settings
from django.db import models
from django.utils import timezone
from django.core.validators import MinLengthValidator


class Article(models.Model):
    project=models.ForeignKey('webapp.Project',related_name='project_id',default=1,blank=True,on_delete=models.CASCADE,verbose_name='Проект')
    description = models.CharField(max_length=2000, null=False, blank=False, verbose_name='Описание',validators=[MinLengthValidator(5)])
    maxdescription = models.TextField(max_length=2000,null=True,blank=False,verbose_name='Подробное описание')
    types = models.ManyToManyField('webapp.Type',related_name='type_key', blank=True, verbose_name='Тип')
    status = models.ForeignKey('Status',related_name='status_key',on_delete=models.CASCADE, verbose_name='Статус')
    publish_at = models.DateTimeField(verbose_name="Время публикации", blank=True, default=timezone.now)
    updated_at = models.DateTimeField(verbose_name='Время изменения', blank=True, default=timezone.now)

    def save(self, **kwargs):
        if not self.publish_at:
            if not self.pk:
                self.publish_at = timezone.now()
            else:
                self.publish_at = Article.objects.get(pk=self.pk).publish_at
        super().save(**kwargs)

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




class Project(models.Model):
    users = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name='user', blank=True)
    name = models.CharField(max_length=40, default='project',verbose_name='Название')
    text = models.TextField(max_length=400, null=True, blank=True, verbose_name='Описание')
    newdate_at = models.DateField(max_length=10, null=True,blank=False, verbose_name='Дата создания')
    enddate_at = models.DateField(max_length=10, null=True,blank=False, verbose_name='Дата выполнения')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Проект'
        verbose_name_plural = 'Проекты'
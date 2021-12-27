import datetime

from django.db import models
from django.forms import ModelForm
from django.urls import reverse


class Department(models.Model):
    title = models.CharField(max_length=100, db_index=True, verbose_name='Отдел')
    slug = models.SlugField(max_length=200, unique=False)
    created = models.DateTimeField(auto_now_add=True)
    update = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ('title',)
        verbose_name = 'Отдел'
        verbose_name_plural = 'Подразделения'
        index_together = (('id', 'slug'),)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('main: post_list_by_department', args=[self.id, self.slug])


class Post(models.Model):
    department = models.ForeignKey('Department', related_name='post', on_delete=models.PROTECT, verbose_name='Отдел')
    title = models.CharField(max_length=100, db_index=True, verbose_name='Должность')
    slug = models.SlugField(max_length=200, unique=False)
    created = models.DateTimeField(auto_now_add=True)
    update = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ('title',)
        verbose_name = 'Должность'
        verbose_name_plural = 'Должности'
        index_together = (('id', 'slug'),)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('main: post_employees', args=[self.id, self.slug])


class Employees(models.Model):
    department = models.ForeignKey('Department', related_name='employees', on_delete=models.PROTECT,
                                   verbose_name='Отдел')
    post = models.ForeignKey('Post', related_name='employees', on_delete=models.PROTECT, verbose_name='Должность')
    title = models.CharField(max_length=100, db_index=True, verbose_name='Ф.И.О.')
    slug = models.SlugField(max_length=200, unique=False)
    started = models.DateField(auto_now_add=False, verbose_name='Пришел на работу')
    created = models.DateTimeField(auto_now_add=True)
    update = models.DateTimeField(auto_now_add=True)

    @property
    def experience(self):
        return datetime.date.today() - self.started

    class Meta:
        ordering = ('title',)
        verbose_name = 'Сотрудник'
        verbose_name_plural = 'Сотрудники'
        index_together = (('id', 'slug'),)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('staff:employees_detail', args=[self.id, self.slug])

    def get_update_url(self):
        return reverse('staff:edit_employees_detail', args=[self.id, self.slug])


class DepartmentForm(ModelForm):
    class Meta:
        model = Department
        fields = ['title']


class PostForm(ModelForm):
    class Meta:
        model = Post
        fields = ['department', 'title']


class EmployeesForm(ModelForm):
    class Meta:
        model = Employees
        fields = ['department', 'post', 'title', 'started']

from django import forms

from staff.models import *


class DepartmentForm(forms.ModelForm):

    def __int__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    class Meta:
        model = Department
        fields = '__all__'


class PostForm(forms.ModelForm):

    def __int__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['department'].empty_label = "Отдел не выбран"

    class Meta:
        model = Post
        fields = '__all__'


class EmployeesForm(forms.ModelForm):

    def __int__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['department'].empty_label = "Отдел не выбран"
        self.fields['post'].empty_label = "Должность не выбрана"

    class Meta:
        model = Employees
        fields = '__all__'


class EditEmployeesForm(forms.ModelForm):

    class Meta:
        model = Employees
        fields = ('department', 'post')


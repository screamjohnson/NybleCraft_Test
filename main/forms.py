from django.contrib.auth import password_validation
from django.core.exceptions import ValidationError
from django import forms

# from .apps import user_registered
from .models import MyUser


class RegisterUserForm(forms.ModelForm):
    email = forms.EmailField(required=True, label='Адрес электронной почты')
    password1 = forms.CharField(label='Пароль', widget=forms.PasswordInput, help_text=password_validation.password_validators_help_text_html())
    password2 = forms.CharField(label='Пароль(Повторно)', widget=forms.PasswordInput, help_text='Введите пароль повторно')

    def clean_password1(self):
        password1 = self.cleaned_data['password1']
        if password1:
            try:
                password_validation.validate_password(password1)
            except forms.ValidationError as error:
                self.add_error('password1', error)
            return password1

    def clean(self):
        super().clean()
        password1 = self.cleaned_data['password1']
        password2 = self.cleaned_data['password2']
        if password1 and password2 and password1 != password2:
            errors = {'password2': ValidationError('Введенные пароли не совпадают', code='password_mismatch')}
            raise ValidationError(errors)

    def save(self, commit=True):
        user = super().save(commit=False)
        user.set_password(self.cleaned_data['password1'])
        user.is_active = False
        user.is_activated = False
        if commit:
            user.save()
        # user_registered.send(RegisterUserForm, instance=user)
        return user


    class Meta:
        model = MyUser
        fields = ('username', 'email', 'password1', 'password2', 'first_name', 'last_name', 'send_messages')


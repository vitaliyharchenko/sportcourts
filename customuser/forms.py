# coding=utf-8
from django import forms
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import ReadOnlyPasswordHashField
from models import User
from utils.forms import BootstrapModelForm, BootstrapForm
from utils.validators import validate_password
from utils.witgets import JasnyImageWidget


class UserCreationForm(BootstrapModelForm):
    error_messages = {
        'duplicate_email': "A user with that email already exists.",
        'password_mismatch': "The two password fields didn't match.",
    }

    password1 = forms.CharField(
        label="Пароль",
        widget=forms.PasswordInput)
    password2 = forms.CharField(
        label="Подтвердите",
        widget=forms.PasswordInput,
        help_text="Введите тот же пароль")

    class Meta:
        model = get_user_model()
        fields = ('email', 'first_name', 'last_name')

    def clean_email(self):
        email = self.cleaned_data["email"]
        try:
            get_user_model().objects.get(email=email)
        except get_user_model().DoesNotExist:
            return email
        raise forms.ValidationError(
            self.error_messages['duplicate_email'],
            code='duplicate_email',
        )

    def clean_password2(self):
        password1 = self.cleaned_data.get("password1")
        password2 = self.cleaned_data.get("password2")
        if password1 and password2 and password1 != password2:
            raise forms.ValidationError(
                self.error_messages['password_mismatch'],
                code='password_mismatch',
            )
        return password2

    def save(self, commit=True):
        user = super(UserCreationForm, self).save(commit=False)
        user.set_password(self.cleaned_data["password1"])
        if commit:
            user.save()
        return user


class UserChangeForm(forms.ModelForm):
    password = ReadOnlyPasswordHashField(label="Password", help_text=
    "Raw passwords are not stored, so there is no way to see "
    "this user's password, but you can change the password "
    "using <a href=\"password/\">this form</a>.")

    class Meta:
        model = get_user_model()
        exclude = ()

    def __init__(self, *args, **kwargs):
        super(UserChangeForm, self).__init__(*args, **kwargs)
        f = self.fields.get('user_permissions', None)
        if f is not None:
            f.queryset = f.queryset.select_related('content_type')

    def clean_password(self):
        return self.initial["password"]


class EmailForm(forms.Form):
    email = forms.EmailField(label='Емейл', max_length=150)


class UserLoginForm(BootstrapForm):
    email = forms.EmailField(label='Email', max_length=150)
    password = forms.CharField(label='Пароль', widget=forms.PasswordInput())


class UserRegistrationForm(BootstrapModelForm):
    # TODO: Override all error messages
    class Meta:
        model = get_user_model()
        fields = User.REGISTRATION_FIELDS
        widgets = {'vkuserid': forms.HiddenInput(),
                   'password': forms.PasswordInput(render_value=False),
                   'email': forms.EmailInput({'readonly': 'True'}),
                   'avatar': JasnyImageWidget()}

    def clean_password(self):
        value = self.cleaned_data['password']
        validate_password(value)
        return value


class UpdateForm(BootstrapModelForm):
    class Meta:
        model = User
        fields = ['avatar', 'first_name', 'last_name', 'sex', 'bdate', 'city', 'phone', 'weight', 'height', 'ampluas']
        widgets = {'ampluas': forms.CheckboxSelectMultiple}


class ChangePasswordForm(BootstrapForm):
    password = forms.CharField(label='Новый пароль', widget=forms.PasswordInput())
    password1 = forms.CharField(label='Еще раз', widget=forms.PasswordInput())

    def clean_password1(self):
        password = self.cleaned_data.get("password")
        password1 = self.cleaned_data.get("password1")
        if password and password1 and password != password1:
            raise forms.ValidationError("Введенные пароли не совпадают", code='password_mismatch',)
        return password1
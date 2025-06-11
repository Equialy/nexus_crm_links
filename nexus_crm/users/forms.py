from django import forms
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UsernameField, AuthenticationForm
from django.contrib.auth.password_validation import password_validators_help_text_html, validate_password
from django.utils.translation import gettext_lazy as _

from users.models import UserProfile


class SignUpForm(forms.ModelForm):

    username = forms.CharField(
        label=_("Имя пользователя"),
        max_length=150,
        widget=forms.TextInput(attrs={'class': 'form-control'})
    )

    email = forms.EmailField(label=_("Email address"),
                             widget=forms.TextInput(attrs={'class': 'form-control'}))


    password1 = forms.CharField(
        label=_("Password"),
        strip=False,
        widget=forms.PasswordInput(attrs={'class': 'form-control'}),
        help_text=_("Пароль должен содержать минимум 4 символа")

    )

    password2 = forms.CharField(
        label=_("Password confirmation"),
        strip=False,
        widget=forms.PasswordInput(attrs={'class': 'form-control'}),
        help_text=_("Enter the same password as before, for verification."),
    )
    class Meta:
        model = UserProfile
        fields = ['username', 'email', 'phone_number']

    def clean_password2(self):
        """
        Проверка совпадения паролей.
        """
        password1 = self.cleaned_data.get('password1')
        password2 = self.cleaned_data.get('password2')
        if password1 and password2 and password1 != password2:
            raise forms.ValidationError(_("Passwords do not match."))
        validate_password(password1)
        return password2

    def save(self, commit=True):
        """
        Переопределяем метод save для сохранения пароля в хэшированном виде.
        """
        user = super().save(commit=False)
        user.set_password(self.cleaned_data["password1"])  # Хэшируем пароль
        if commit:
            user.save()
        return user


class LoginUserForm(AuthenticationForm):
    username = forms.CharField(
        label=_("Email"),
        max_length=150,
        # help_text=_(
        #     "Letters, digits and @/./+/-/_ only."
        # ),
        widget=forms.TextInput(attrs={'class': 'form-control'})
    )
    password = forms.CharField(
        label=_("Password"),
        strip=False,
        widget=forms.PasswordInput(attrs={'class': 'form-control'}),
        help_text=_("Пароль должен содержать минимум 4 символа")

    )

    class Meta:
        model = UserProfile
        fields = ['username', 'password']


class ProfileUserForm(forms.ModelForm):
    username = forms.CharField(
        label=_("Имя пользователя"),
        max_length=150,
        help_text=_(
            "Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only."
        ),
        widget=forms.TextInput(attrs={'class': 'form-control'})
    )


    email = forms.EmailField(label=_("Email address"),
                             widget=forms.TextInput(attrs={'class': 'form-control'}))
    class Meta:
        model = UserProfile
        fields = ['username', 'email', "password"  ]


class PasswordResetRequestForm(forms.Form):
    email = forms.EmailField(
        label="Email",
        max_length=50,
        widget=forms.EmailInput(attrs={'class': 'input-register form-control',
                                       'placeholder': 'Your email'})
    )

class PasswordResetConfirmForm(forms.Form):
    new_password1 = forms.CharField(
        label="New Password",
        widget=forms.PasswordInput(attrs={'class': 'input-register form-control',
                                          'placeholder': 'New password'})
    )
    new_password2 = forms.CharField(
        label="Confirm New Password",
        widget=forms.PasswordInput(attrs={'class': 'input-register form-control',
                                          'placeholder': 'Confirm new password'})
    )

    def clean(self):
        cleaned_data = super().clean()
        new_password1 = cleaned_data.get('new_password1')
        new_password2 = cleaned_data.get('new_password2')
        if new_password1 and new_password2 and new_password1 != new_password2:
            raise forms.ValidationError("Passwords do not match.")
        return cleaned_data
from django import forms
from django.contrib.auth.models import User
from account.models import Profile


class UserRegistrationForm(forms.ModelForm):
    password = forms.CharField(label='Parol',
                               widget=forms.PasswordInput)
    password_2 = forms.CharField(label="parolni takrorlang",
                                 widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ["username", "first_name", 'email']

    def clean_password2(self):
        data = self.cleaned_data
        if data["password"] != data["password"]:
            raise forms.ValidationError("Ikkala parolingiz ham bir-biriga teng bo'lishi kerak !")

class UserEditForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'email']

class ProfileEditForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['data_of_birth','photo']
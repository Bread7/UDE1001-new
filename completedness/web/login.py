from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class NewUserForm(UserCreationForm):
    email = forms.EmailField(required=True)

    class Meta:
        model = User
        fields = ("username","email","password1", 'password2')

    def save(self, commit=True):
        newUser = super(NewUserForm, self).save(commit=False)
        newUser.email = self.cleaned_data['email']
        if commit:
            newUser.save()
        return newUser
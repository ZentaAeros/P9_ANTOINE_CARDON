from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm, UsernameField
from django.forms import TextInput

from django import forms


class UserLoginForm(AuthenticationForm):
    def __init__(self, *args, **kwargs):
        super(UserLoginForm, self).__init__(*args, **kwargs)

    username = UsernameField(widget=forms.TextInput(
        attrs={'class': 'form-control', 'style':"max-width:300px"}))
    password = forms.CharField(widget=forms.PasswordInput(
        attrs={
            'class': 'form-control',
            'style':"max-width:300px"
        }
))

class SignupForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = get_user_model()
        fields = ['username', 'first_name', 'last_name']
        widgets = {
            'username': TextInput(attrs={
                'class': "form-control",
                'style': "max-width:300px"
            }),
            'first_name': TextInput(attrs={
                'class': "form-control",
                'style': "max-width:300px"
            }
            ),
            'last_name': TextInput(attrs={
                'class': "form-control",
                'style': "max-width:300px"
            })
        }

class SearchUser(forms.Form):
    user = forms.CharField(max_length=250, label="Saisissez le nom d'utilisateur ")
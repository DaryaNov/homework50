from django.contrib.auth.forms import UserCreationForm
from django.core.exceptions import ValidationError
from django import forms


def at_least_5(string):
    if len(string) <=0:
        raise ValidationError('This value is too short!')

class MyUserCreationForm(UserCreationForm):
    last_name=forms.CharField(validators=(at_least_5,))
    email=forms.EmailField(required=True)

    class Meta(UserCreationForm.Meta):
        fields = ['username', 'password1', 'password2',
                  'first_name', 'last_name', 'email']

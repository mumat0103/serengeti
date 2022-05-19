from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from .models import User

class UserRegistrationForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = User
        fields = [
            'username',
        ]

class UserConfirmationForm(AuthenticationForm):
    class Meta(UserCreationForm.Meta):
        model = User
        fields = [
            'username'
        ]
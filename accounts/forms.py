from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm

class RegisterForm(UserCreationForm):
    # Kullanıcı kayıt formu
    class Meta:
        model = User  # Kullanıcı modelini kullan
        fields = ['username', 'email', 'password1', 'password2']  # Kullanıcının hangi alanlarını içereceğini belirle

class LoginForm(AuthenticationForm):
    # Kullanıcı giriş formu
    class Meta:
        model = User  # Kullanıcı modelini kullan
        fields = ['username', 'password']  # Kullanıcının hangi alanlarını içereceğini belirle

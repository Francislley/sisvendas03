from django import forms
from pessoas.models import Pessoa

class PessoaForm(forms.ModelForm):
	class Meta:
		model = Pessoa

class LoginForm(forms.Form):
    login = forms.CharField(max_length=100, required=True)
    senha = forms.CharField(widget=forms.PasswordInput, required=True)
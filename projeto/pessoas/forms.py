from django import forms
from pessoas.models import Pessoa

class PessoaForm(forms.ModelForm):
	class Meta:
		model = Pessoa
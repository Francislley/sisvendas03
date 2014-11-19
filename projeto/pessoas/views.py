from django.shortcuts import render, HttpResponseRedirect, HttpResponse
from pessoas.forms import PessoaForm, LoginForm
from pessoas.models import Pessoa
from django.contrib.auth import authenticate, logout, login as meu_login
from django.contrib.auth.decorators import login_required

def index(request):
	return render(request, 'index.html')

@login_required()
def cadastro(request):
	form = PessoaForm()
	return render(request, 'cadastro.html', {'form':form})

@login_required()
def ConsultaUsuarios(request):
	pessoas = Pessoa.objects.all()
	return render(request, 'usuarios.html', {'pessoas':pessoas})

def validar(request):
	if request.method == 'POST':
		form = PessoaForm(request.POST)

		if form.is_valid():
			pessoa = Pessoa(**form.cleaned_data)
			pessoa.save()

			return render(request, 'validar.html', {'form':form })


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


def login(request):
    form = LoginForm()
    return render(request, 'login.html',{'form':form});

def logoff(request):
	logout(request)
	return HttpResponseRedirect('/')

def validarlogin(request):
	if request.method == 'POST':
		form = LoginForm(request.POST)

		if form.is_valid():
			pessoa = authenticate(username=form.data['login'], password=form.data['senha'])

			if pessoa is not None:
				if pessoa.is_active:
					meu_login(request, pessoa)
					return HttpResponseRedirect('/')
				else:
					return render(request, 'login.html', {'form': form})
			else:
				return render(request, 'login.html', {'form': form})
		else:
			return render(request, 'login.html', {'form': form})
	else:
		return HttpResponseRedirect('/login/')

def excluir(request, pk=0):
    try:
        pessoa = Pessoa.objects.get(pk=pk)
        pessoa.delete()
        return HttpResponseRedirect('/ConsultaUsuarios/')
    except:
        return HttpResponseRedirect('/ConsultaUsuarios/')
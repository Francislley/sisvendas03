from django.shortcuts import render, HttpResponseRedirect, HttpResponse
from pessoas.forms import PessoaForm, LoginForm
from pessoas.models import Pessoa
from django.contrib.auth import authenticate, logout, login as meu_login
from django.contrib.auth.decorators import login_required
from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('pessoas.views',
    url(r'^$', 'index'),
    url(r'^cadastro/$', 'cadastro'),
	url(r'^validar/$', 'validar'),
	url(r'^ConsultaUsuarios/$', 'ConsultaUsuarios'),
	url(r'^editar/(?P<pk>\d+)/$', 'editar'),
    url(r'^salvar/$', 'salvar'),
    url(r'^excluir/(?P<pk>\d+)/$', 'excluir'),
	url(r'^login/$', 'login'),
	url(r'^logoff/$', 'logoff'),
	url(r'^validarlogin/$', 'validarlogin'),
)

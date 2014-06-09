from django.conf.urls import patterns, include, url


urlpatterns = patterns('pessoas.views',
    url(r'^aluno/','criar_aluno',name='criar_aluno'),
    url(r'^alunos/','alunos',name='alunos'),

)

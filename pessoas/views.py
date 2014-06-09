from django.shortcuts import render
from django.http import  HttpResponseRedirect
from pessoas.forms import AlunoForm
from pessoas.models import Aluno
# Create your views here.

def criar_aluno(request):
    if request.method == 'POST':
        return salvar_aluno(request)
    else : 
        return novo_aluno(request)
def salvar_aluno(request):
    form = AlunoForm(request.POST)
    if not form.is_valid():
        return render(request, 'pessoas/aluno_form.html',
            {'form':form})
    obj = form.save()
    return HttpResponseRedirect('/pessoa/alunos')

def novo_aluno(request):
    return render(request, 'pessoas/aluno_form.html',
        {'form':AlunoForm()})

def alunos(request):
    return render(request, 'pessoas/alunos.html',{'alunos':Aluno.objects.all()})
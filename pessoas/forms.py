from django import forms
from pessoas.models import Aluno
class AlunoForm(forms.ModelForm):
	class Meta:
		model = Aluno
from django.db import models

class Aluno(models.Model):
	name = models.CharField('Nome',max_length=50)

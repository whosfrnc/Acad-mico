from django.contrib import admin

from app.models import AreaDoSaber, Avaliacao, Cidade, Coordenador, Curso, Diretor, Disciplina, DisciplinasPorCurso, Estudante, Frequencia, InstituicaoDeEnsino, Matricula, Ocorrencia, PeriodoDeCurso, Professor, TipoDeAvaliacao, Turma
admin.site.register(Professor)
admin.site.register(Estudante)
admin.site.register(Coordenador)
admin.site.register(Diretor)
admin.site.register(InstituicaoDeEnsino)
admin.site.register(AreaDoSaber)
admin.site.register(Curso)
admin.site.register(PeriodoDeCurso)
admin.site.register(Disciplina)
admin.site.register(Matricula)
admin.site.register(Avaliacao)
admin.site.register(Frequencia)
admin.site.register(Turma)
admin.site.register(Cidade)
admin.site.register(Ocorrencia)
admin.site.register(DisciplinasPorCurso)
admin.site.register(TipoDeAvaliacao)


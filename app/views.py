from django.shortcuts import render
from django.views import View
from .models import Professor, Estudante, Coordenador, Diretor, InstituicaoDeEnsino, AreaDoSaber, Curso, PeriodoDeCurso, Disciplina, Matricula, Avaliacao, Frequencia, Turma, Cidade, Ocorrencia, DisciplinasPorCurso, TipoDeAvaliacao

class IndexView(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'index.html')

class ProfessoresView(View):
    def get(self, request, *args, **kwargs):
        professores = Professor.objects.all()
        return render(request, 'professores.html', {'professores': professores})
    
class EstudantesView(View):
    def get(self, request, *args, **kwargs):
        estudantes = Estudante.objects.all()
        return render(request, 'estudantes.html', {'estudantes': estudantes})

class CoordenadoresView(View):
    def get(self, request, *args, **kwargs):
        coordenadores = Coordenador.objects.all()
        return render(request, 'coordenadores.html', {'coordenadores': coordenadores})

class DiretoresView(View):
    def get(self, request, *args, **kwargs):
        diretores = Diretor.objects.all()
        return render(request, 'diretores.html', {'diretores': diretores})

class InstituicoesDeEnsinoView(View):
    def get(self, request, *args, **kwargs):
        instituicoes = InstituicaoDeEnsino.objects.all()
        return render(request, 'instituicoes.html', {'instituicoes': instituicoes})

class AreasDoSaberView(View):
    def get(self, request, *args, **kwargs):
        areas = AreaDoSaber.objects.all()
        return render(request, 'areas.html', {'areas': areas})

class CursosView(View):
    def get(self, request, *args, **kwargs):
        cursos = Curso.objects.all()
        return render(request, 'cursos.html', {'cursos': cursos})

class PeriodosDeCursoView(View):
    def get(self, request, *args, **kwargs):
        periodos = PeriodoDeCurso.objects.all()
        return render(request, 'periodos.html', {'periodos': periodos})

class DisciplinasView(View):
    def get(self, request, *args, **kwargs):
        disciplinas = Disciplina.objects.all()
        return render(request, 'disciplinas.html', {'disciplinas': disciplinas})

class MatriculasView(View):
    def get(self, request, *args, **kwargs):
        matriculas = Matricula.objects.all()
        return render(request, 'matriculas.html', {'matriculas': matriculas})

class AvaliacoesView(View):
    def get(self, request, *args, **kwargs):
        avaliacoes = Avaliacao.objects.all()
        return render(request, 'avaliacoes.html', {'avaliacoes': avaliacoes})

class FrequenciasView(View):
    def get(self, request, *args, **kwargs):
        frequencias = Frequencia.objects.all()
        return render(request, 'frequencias.html', {'frequencias': frequencias})

class TurmasView(View):
    def get(self, request, *args, **kwargs):
        turmas = Turma.objects.all()
        return render(request, 'turmas.html', {'turmas': turmas})

class CidadesView(View):
    def get(self, request, *args, **kwargs):
        cidades = Cidade.objects.all()
        return render(request, 'cidades.html', {'cidades': cidades})

class OcorrenciasView(View):
    def get(self, request, *args, **kwargs):
        ocorrencias = Ocorrencia.objects.all()
        return render(request, 'ocorrencias.html', {'ocorrencias': ocorrencias})

class DisciplinasPorCursoView(View):
    def get(self, request, *args, **kwargs):
        disciplinas_por_curso = DisciplinasPorCurso.objects.all()
        return render(request, 'disciplinas_por_curso.html', {'disciplinas_por_curso': disciplinas_por_curso})

class TiposDeAvaliacaoView(View):
    def get(self, request, *args, **kwargs):
        tipos_de_avaliacao = TipoDeAvaliacao.objects.all()
        return render(request, 'tipos_de_avaliacao.html', {'tipos_de_avaliacao': tipos_de_avaliacao})

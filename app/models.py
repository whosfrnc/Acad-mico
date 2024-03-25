from django.db import models

class Pessoa(models.Model):
    nome = models.CharField(max_length=100, verbose_name="Nome")
    pai = models.CharField(max_length=100, verbose_name="Nome do pai")
    mae = models.CharField(max_length=100, verbose_name="Nome da mãe")
    cpf = models.CharField(max_length=11, unique=True, verbose_name="CPF")
    data_nasc = models.DateField(verbose_name="Data de nascimento")
    email = models.EmailField(verbose_name="Email")
    cidade = models.ForeignKey('Cidade', on_delete=models.CASCADE, verbose_name="Cidade")

    def __str__(self):
        return self.nome

class Professor(Pessoa):
    ocupacao = models.CharField(max_length=100, verbose_name="Ocupação")

    def __str__(self):
        return self.nome

class Estudante(Pessoa):
    ocupacao = models.CharField(max_length=100, verbose_name="Ocupação")

    def __str__(self):
        return self.nome

class Coordenador(Pessoa):
    ocupacao = models.CharField(max_length=100, verbose_name="Ocupação")

    def __str__(self):
        return self.nome

class Diretor(Pessoa):
    ocupacao = models.CharField(max_length=100, verbose_name="Ocupação")

    def __str__(self):
        return self.nome

class InstituicaoDeEnsino(models.Model):
    nome = models.CharField(max_length=100, verbose_name="Nome")
    site = models.URLField(verbose_name="Site")
    telefone = models.CharField(max_length=20, verbose_name="Telefone")
    cidade = models.ForeignKey('Cidade', on_delete=models.CASCADE, verbose_name="Cidade")

    def __str__(self):
        return self.nome

class AreaDoSaber(models.Model):
    nome = models.CharField(max_length=100, verbose_name="Nome")

    def __str__(self):
        return self.nome

class Curso(models.Model):
    nome = models.CharField(max_length=100, verbose_name="Nome")
    carga_horaria_total = models.IntegerField(verbose_name="Carga Horária Total")
    duracao_meses = models.IntegerField(verbose_name="Duração em Meses")
    areas_saber = models.ManyToManyField(AreaDoSaber, verbose_name="Áreas do Saber")
    instituicao = models.ForeignKey(InstituicaoDeEnsino, on_delete=models.CASCADE, verbose_name="Instituição")

    def __str__(self):
        return self.nome

class PeriodoDeCurso(models.Model):
    nome = models.CharField(max_length=100, verbose_name="Nome")

    def __str__(self):
        return self.nome

class Disciplina(models.Model):
    nome = models.CharField(max_length=100, verbose_name="Nome")
    area_saber = models.ForeignKey(AreaDoSaber, on_delete=models.CASCADE, verbose_name="Área do Saber")

    def __str__(self):
        return self.nome


class Avaliacao(models.Model):
    descricao = models.TextField(verbose_name="Descrição")
    curso = models.ForeignKey(Curso, on_delete=models.CASCADE, verbose_name="Curso")
    disciplina = models.ForeignKey(Disciplina, on_delete=models.CASCADE, verbose_name="Disciplina")



class Turma(models.Model):
    PERIODO_CHOICES = [
        ('matutino', 'Matutino'),
        ('vespertino', 'Vespertino'),
        ('noturno', 'Noturno'),
    ]
    nome = models.CharField(max_length=100, verbose_name="Nome")
    periodo = models.CharField(max_length=20, choices=PERIODO_CHOICES, verbose_name="Período")

class Cidade(models.Model):
    nome = models.CharField(max_length=100, verbose_name="Nome da cidade")
    uf = models.CharField(max_length=2, verbose_name="UF")

    def __str__(self):
        return f"{self.nome}, {self.uf}"



class DisciplinasPorCurso(models.Model):
    disciplina = models.ForeignKey(Disciplina, on_delete=models.CASCADE, verbose_name="Disciplina")
    carga_horaria = models.IntegerField(verbose_name="Carga Horária")
    curso = models.ForeignKey(Curso, on_delete=models.CASCADE, verbose_name="Curso")
    periodo = models.ForeignKey(PeriodoDeCurso, on_delete=models.CASCADE, verbose_name="Período")

class TipoDeAvaliacao(models.Model):
    nome = models.CharField(max_length=100, verbose_name="Nome")

    def __str__(self):
        return self.nome
    

class Frequencia(models.Model):
    curso = models.ForeignKey(Curso, on_delete=models.CASCADE, verbose_name="Curso")
    disciplina = models.ForeignKey(Disciplina, on_delete=models.CASCADE, verbose_name="Disciplina")
    Pessoa = models.ForeignKey('Pessoa', on_delete=models.CASCADE, verbose_name="Pessoa")
    numero_faltas = models.IntegerField(verbose_name="Número de Faltas")

class Matricula(models.Model):
    instituicao = models.ForeignKey(InstituicaoDeEnsino, on_delete=models.CASCADE, verbose_name="Instituição")
    curso = models.ForeignKey(Curso, on_delete=models.CASCADE, verbose_name="Curso")
    Pessoa = models.ForeignKey('Pessoa', on_delete=models.CASCADE, verbose_name="Pessoa")
    data_inicio = models.DateField(verbose_name="Data de Início")
    data_previsao_termino = models.DateField(verbose_name="Data de Previsão de Término")

class Ocorrencia(models.Model):
    descricao = models.TextField(verbose_name="Descrição")
    data = models.DateField(verbose_name="Data")
    curso = models.ForeignKey(Curso, on_delete=models.CASCADE, verbose_name="Curso")
    disciplina = models.ForeignKey(Disciplina, on_delete=models.CASCADE, verbose_name="Disciplina")
    Pessoa = models.ForeignKey('Pessoa', on_delete=models.CASCADE, verbose_name="Pessoa")


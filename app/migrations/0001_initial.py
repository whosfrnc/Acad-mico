# Generated by Django 5.0.3 on 2024-03-25 17:08

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='AreaDoSaber',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=100, verbose_name='Nome')),
            ],
        ),
        migrations.CreateModel(
            name='Cidade',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=100, verbose_name='Nome da cidade')),
                ('uf', models.CharField(max_length=2, verbose_name='UF')),
            ],
        ),
        migrations.CreateModel(
            name='Pessoa',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=100, verbose_name='Nome')),
                ('pai', models.CharField(max_length=100, verbose_name='Nome do pai')),
                ('mae', models.CharField(max_length=100, verbose_name='Nome da mãe')),
                ('cpf', models.CharField(max_length=11, unique=True, verbose_name='CPF')),
                ('data_nasc', models.DateField(verbose_name='Data de nascimento')),
                ('email', models.EmailField(max_length=254, verbose_name='Email')),
                ('cidade', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.cidade', verbose_name='Cidade')),
            ],
        ),
        migrations.CreateModel(
            name='PeriodoDeCurso',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=100, verbose_name='Nome')),
            ],
        ),
        migrations.CreateModel(
            name='TipoDeAvaliacao',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=100, verbose_name='Nome')),
            ],
        ),
        migrations.CreateModel(
            name='Turma',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=100, verbose_name='Nome')),
                ('periodo', models.CharField(choices=[('matutino', 'Matutino'), ('vespertino', 'Vespertino'), ('noturno', 'Noturno')], max_length=20, verbose_name='Período')),
            ],
        ),
        migrations.CreateModel(
            name='Coordenador',
            fields=[
                ('pessoa_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='app.pessoa')),
                ('ocupacao', models.CharField(max_length=100, verbose_name='Ocupação')),
            ],
            bases=('app.pessoa',),
        ),
        migrations.CreateModel(
            name='Diretor',
            fields=[
                ('pessoa_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='app.pessoa')),
                ('ocupacao', models.CharField(max_length=100, verbose_name='Ocupação')),
            ],
            bases=('app.pessoa',),
        ),
        migrations.CreateModel(
            name='Estudante',
            fields=[
                ('pessoa_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='app.pessoa')),
                ('ocupacao', models.CharField(max_length=100, verbose_name='Ocupação')),
            ],
            bases=('app.pessoa',),
        ),
        migrations.CreateModel(
            name='Professor',
            fields=[
                ('pessoa_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='app.pessoa')),
                ('ocupacao', models.CharField(max_length=100, verbose_name='Ocupação')),
            ],
            bases=('app.pessoa',),
        ),
        migrations.CreateModel(
            name='Curso',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=100, verbose_name='Nome')),
                ('carga_horaria_total', models.IntegerField(verbose_name='Carga Horária Total')),
                ('duracao_meses', models.IntegerField(verbose_name='Duração em Meses')),
                ('areas_saber', models.ManyToManyField(to='app.areadosaber', verbose_name='Áreas do Saber')),
            ],
        ),
        migrations.CreateModel(
            name='Disciplina',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=100, verbose_name='Nome')),
                ('area_saber', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.areadosaber', verbose_name='Área do Saber')),
            ],
        ),
        migrations.CreateModel(
            name='Avaliacao',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('descricao', models.TextField(verbose_name='Descrição')),
                ('curso', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.curso', verbose_name='Curso')),
                ('disciplina', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.disciplina', verbose_name='Disciplina')),
            ],
        ),
        migrations.CreateModel(
            name='Frequencia',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('numero_faltas', models.IntegerField(verbose_name='Número de Faltas')),
                ('Pessoa', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.pessoa', verbose_name='Pessoa')),
                ('curso', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.curso', verbose_name='Curso')),
                ('disciplina', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.disciplina', verbose_name='Disciplina')),
            ],
        ),
        migrations.CreateModel(
            name='InstituicaoDeEnsino',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=100, verbose_name='Nome')),
                ('site', models.URLField(verbose_name='Site')),
                ('telefone', models.CharField(max_length=20, verbose_name='Telefone')),
                ('cidade', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.cidade', verbose_name='Cidade')),
            ],
        ),
        migrations.AddField(
            model_name='curso',
            name='instituicao',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.instituicaodeensino', verbose_name='Instituição'),
        ),
        migrations.CreateModel(
            name='Matricula',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('data_inicio', models.DateField(verbose_name='Data de Início')),
                ('data_previsao_termino', models.DateField(verbose_name='Data de Previsão de Término')),
                ('Pessoa', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.pessoa', verbose_name='Pessoa')),
                ('curso', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.curso', verbose_name='Curso')),
                ('instituicao', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.instituicaodeensino', verbose_name='Instituição')),
            ],
        ),
        migrations.CreateModel(
            name='Ocorrencia',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('descricao', models.TextField(verbose_name='Descrição')),
                ('data', models.DateField(verbose_name='Data')),
                ('Pessoa', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.pessoa', verbose_name='Pessoa')),
                ('curso', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.curso', verbose_name='Curso')),
                ('disciplina', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.disciplina', verbose_name='Disciplina')),
            ],
        ),
        migrations.CreateModel(
            name='DisciplinasPorCurso',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('carga_horaria', models.IntegerField(verbose_name='Carga Horária')),
                ('curso', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.curso', verbose_name='Curso')),
                ('disciplina', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.disciplina', verbose_name='Disciplina')),
                ('periodo', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.periododecurso', verbose_name='Período')),
            ],
        ),
    ]

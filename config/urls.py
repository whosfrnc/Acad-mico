"""
URL configuration for config project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import include, path
from app.views import * 
from django.views.generic import TemplateView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', TemplateView.as_view(template_name='index.html'),name='index'),
    path('Professor/', ProfessoresView.as_view() ,name='Professor'),
    path('areas/', AreasDoSaberView.as_view(), name='areas'),
    path('avaliacoes/', AvaliacoesView.as_view(),
    name='avaliacoes'),
    path('cidade/', CidadesView.as_view(),
    name='cidade'),
    path('diretor/', DiretoresView.as_view(), name='diretor'),
    path('estudante/', EstudantesView.as_view(),
    name='estudante'),
    path('cursos/', CursosView.as_view(),
    name='cursos'),
    path('frequencias/', FrequenciasView.as_view(),
    name='frequencias'),
     path('instituicaoensino/', InstituicoesDeEnsinoView.as_view(),
    name='instituicaoensino'),
      path('coordenador/', CoordenadoresView.as_view(),
    name='coordenador'),
       path('periododecurso/', PeriodosDeCursoView.as_view(),
    name='periododecurso'),
        path('disciplina/', DisciplinasView.as_view(),
    name='disciplina'),
         path('matricula/', MatriculasView.as_view(),
    name='matricula'),
          path('turma/', TurmasView.as_view(),
    name='turma'),
     path('tipodeavaliacao/',TiposDeAvaliacaoView.as_view(),
    name='tipodeavaliacao'),
      path('disciplinasporcurso/', DisciplinasPorCursoView.as_view(),
    name='disciplinasporcurso'),
      path('ocorrencia/', OcorrenciasView.as_view(),
    name='ocorrencia'),
]

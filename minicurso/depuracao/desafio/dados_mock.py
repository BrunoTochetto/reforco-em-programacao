# =====================================================================
# SISTEMA DE GERENCIAMENTO ESCOLAR - GERADOR DE DADOS MOCK
# Criação de dados iniciais fictícios para testes de depuração
# =====================================================================

from models.aluno import Aluno
from models.professor import Professor
from models.turma import Turma

def carregar_dados_sistema():
    """
    Instancia alunos, professores e turmas pré-configurados e vincula-os.
    Retorna três listas: (alunos, professores, turmas)
    """
    # 1. Instanciando Alunos
    alunos = [
        Aluno(101, "Ana Silva"),
        Aluno(102, "Bruno Strach"),
        Aluno(103, "Carlos Oliveira"),
        Aluno(104, "Daniela Costa")
    ]

    # 2. Instanciando Professores
    professores = [
        Professor(201, "Prof. Marcos", "Matemática"),
        Professor(202, "Profª. Sandra", "História"),
        Professor(203, "Prof. Ricardo", "Geografia")
    ]

    # 3. Instanciando Turmas (Vinculadas aos professores correspondentes)
    turmas = [
        Turma(1, "Matemática 1º Ano", professores[0]),
        Turma(2, "História 1º Ano", professores[1]),
        Turma(3, "Geografia 1º Ano", professores[2])
    ]

    # Mapeando alunos por ID para facilitar as matrículas de teste
    alunos_map = {}
    for aluno in alunos:
        alunos_map[aluno.id] = aluno

    # 4. Matriculando alunos nas turmas
    # Matemática (ID 1) recebe Ana (101), Bruno (102), Carlos (103)
    turmas[0].adicionar_aluno(alunos_map[101])
    turmas[0].adicionar_aluno(alunos_map[102])
    turmas[0].adicionar_aluno(alunos_map[103])

    # História (ID 2) recebe Ana (101), Bruno (102), Daniela (104)
    turmas[1].adicionar_aluno(alunos_map[101])
    turmas[1].adicionar_aluno(alunos_map[102])
    turmas[1].adicionar_aluno(alunos_map[104])

    # Geografia (ID 3) recebe Ana (101), Carlos (103), Daniela (104)
    turmas[2].adicionar_aluno(alunos_map[101])
    turmas[2].adicionar_aluno(alunos_map[103])
    turmas[2].adicionar_aluno(alunos_map[104])

    # 5. Lançando Notas iniciais de teste (Para testar médias e boletins)
    
    # Notas da Ana (101) - Turmas: Matemática (1), História (2), Geografia (3)
    turmas[0].registrar_nota_aluno(101, 10.0)
    turmas[0].registrar_nota_aluno(101, 10.0)

    turmas[1].registrar_nota_aluno(101, 8.0)
    turmas[1].registrar_nota_aluno(101, 5.0)

    turmas[2].registrar_nota_aluno(101, 4.0)
    turmas[2].registrar_nota_aluno(101, 4.0)

    # Notas do Bruno (102) - Turmas: Matemática (1), História (2)
    turmas[0].registrar_nota_aluno(102, 9.0)
    turmas[0].registrar_nota_aluno(102, 5.0)

    turmas[1].registrar_nota_aluno(102, 7.0)
    turmas[1].registrar_nota_aluno(102, 9.0)

    # Notas do Carlos (103) - Turmas: Matemática (1), Geografia (3)
    turmas[0].registrar_nota_aluno(103, 6.0)
    turmas[0].registrar_nota_aluno(103, 8.0)

    turmas[2].registrar_nota_aluno(103, 10.0)
    turmas[2].registrar_nota_aluno(103, 10.0)

    # Notas da Daniela (104) - Turmas: História (2), Geografia (3)
    turmas[1].registrar_nota_aluno(104, 8.5)
    turmas[1].registrar_nota_aluno(104, 6.5)

    turmas[2].registrar_nota_aluno(104, 5.0)
    turmas[2].registrar_nota_aluno(104, 7.0)

    return alunos, professores, turmas

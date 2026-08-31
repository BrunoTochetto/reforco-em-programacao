# =====================================================================
# SISTEMA DE GERENCIAMENTO ESCOLAR - INTERFACE PRINCIPAL
# =====================================================================

import sys
from models.aluno import Aluno
from models.professor import Professor
from models.turma import Turma
from dados_mock import carregar_dados_sistema

ALUNOS = []
PROFESSORES = []
TURMAS = []

# Funções auxiliares para busca de objetos
def buscar_aluno_por_id(aluno_id):
    for aluno in ALUNOS:
        if aluno.id == aluno_id:
            return aluno
    return None

def buscar_professor_por_id(prof_id):
    for prof in PROFESSORES:
        if prof.id == prof_id:
            return prof
    return None

def buscar_turma_por_id(turma_id):
    for turma in TURMAS:
        if turma.id == turma_id:
            return turma
    return None


# =====================================================================
# 1. ÁREA DE ADMINISTRAÇÃO
# =====================================================================

def menu_administracao():
    while True:
        print("\n================== ÁREA ADMINISTRATIVA ==================")
        print("1. Cadastrar Novo Aluno")
        print("2. Listar Todos os Alunos")
        print("3. Atualizar Dados de Aluno")
        print("4. Excluir Aluno do Sistema")
        print("-" * 55)
        print("5. Cadastrar Novo Professor")
        print("6. Listar Todos os Professores")
        print("7. Atualizar Dados de Professor")
        print("8. Excluir Professor do Sistema")
        print("-" * 55)
        print("9. Matricular Aluno em uma Turma")
        print("10. Voltar ao Menu Principal")
        print("=========================================================")
        
        opcao = input("Selecione uma opção (1-10): ").strip()
        
        if opcao == "1":
            print("\n--- CADASTRAR ALUNO ---")
            try:
                aluno_id = Aluno.id + 1

                nome = input("Digite o nome completo do aluno: ").strip()
                if not nome:
                    print("Erro: O nome do aluno não pode ser vazio.")
                    continue
                novo_aluno = Aluno(aluno_id, nome)
                ALUNOS.append(novo_aluno)
                print(f"Sucesso: Aluno '{nome}' cadastrado com sucesso!")
                Aluno.id += 1

            except ValueError:
                print("Erro: O ID deve ser um número inteiro.")
                
        elif opcao == "2":
            print("\n--- LISTA DE ALUNOS REGISTRADOS ---")
            if len(ALUNOS) == 0:
                print("Não há alunos cadastrados no sistema.")
            else:
                print(f"{'ID':<10} | {'NOME DO ALUNO':<30} | {'FALTAS':<8}")
                print("-" * 55)
                for aluno in ALUNOS:
                    print(f"{aluno.id:<10} | {aluno.nome:<30} | {aluno.faltas:<8}")
                    
        elif opcao == "3":
            print("\n--- ATUALIZAR ALUNO ---")
            try:
                aluno_id = int(input("Digite o ID do aluno a ser atualizado: "))
                aluno = buscar_aluno_por_id(aluno_id)
                if aluno is None:
                    print("Erro: Aluno não localizado.")
                    continue
                novo_nome = input(f"Novo nome para '{aluno.nome}' (Pressione enter para manter): ").strip()
                if novo_nome:
                    aluno.nome = novo_nome
                print("Sucesso: Cadastro do aluno atualizado!")
            except ValueError:
                print("Erro: ID inválido.")
                
        elif opcao == "4":
            print("\n--- EXCLUIR ALUNO ---")
            try:
                aluno_id = int(input("Digite o ID do aluno a ser excluído: "))
                aluno = buscar_aluno_por_id(aluno_id)
                if aluno is None:
                    print("Erro: Aluno não localizado.")
                    continue
                ALUNOS.remove(aluno)
                # Remove o aluno de todas as turmas que ele estava matriculado
                for turma in TURMAS:
                    if aluno in turma.alunos:
                        turma.alunos.remove(aluno)
                print(f"Sucesso: Aluno '{aluno.nome}' removido do sistema!")
            except ValueError:
                print("Erro: ID inválido.")
                
        elif opcao == "5":
            print("\n--- CADASTRAR PROFESSOR ---")
            try:
                prof_id = Professor.id + 1
                nome = input("Digite o nome completo do professor: ").strip()
                especialidade = input("Digite a especialidade/disciplina: ").strip()
                if not nome or not especialidade:
                    print("Erro: Nome e especialidade são campos obrigatórios.")
                    continue
                novo_prof = Professor(prof_id, nome, especialidade)
                PROFESSORES.append(novo_prof)
                
                # Cria automaticamente uma turma para a disciplina deste professor
                turma_id = len(TURMAS) + 1
                nova_turma = Turma(turma_id, f"{especialidade} {turma_id}º Ano", novo_prof)
                TURMAS.append(nova_turma)
                
                print(f"Sucesso: Professor '{nome}' cadastrado!")
                Professor.id += 1
                print(f"Turma criada automaticamente: '{nova_turma.nome}' (ID: {nova_turma.id})")

            except ValueError:
                print("Erro: O ID deve ser um número inteiro.")
                
        elif opcao == "6":
            print("\n--- LISTA DE PROFESSORES REGISTRADOS ---")
            if len(PROFESSORES) == 0:
                print("Não há professores cadastrados no sistema.")
            else:
                print(f"{'ID':<10} | {'NOME DO PROFESSOR':<30} | {'DISCIPLINA':<20}")
                print("-" * 65)
                for prof in PROFESSORES:
                    print(f"{prof.id:<10} | {prof.nome:<30} | {prof.especialidade:<20}")
                    
        elif opcao == "7":
            print("\n--- ATUALIZAR PROFESSOR ---")
            try:
                prof_id = int(input("Digite o ID do professor a ser atualizado: "))
                prof = buscar_professor_por_id(prof_id)
                if prof is None:
                    print("Erro: Professor não localizado.")
                    continue
                novo_nome = input(f"Novo nome para '{prof.nome}' (Pressione enter para manter): ").strip()
                if novo_nome:
                    prof.nome = novo_nome
                nova_esp = input(f"Nova especialidade para '{prof.especialidade}' (Pressione enter para manter): ").strip()
                if nova_esp:
                    prof.especialidade = nova_esp
                print("Sucesso: Cadastro do professor atualizado!")
            except ValueError:
                print("Erro: ID inválido.")
                
        elif opcao == "8":
            print("\n--- EXCLUIR PROFESSOR ---")
            try:
                prof_id = int(input("Digite o ID do professor a ser excluído: "))
                prof = buscar_professor_por_id(prof_id)
                if prof is None:
                    print("Erro: Professor não localizado.")
                    continue
                PROFESSORES.remove(prof)
                # Remove as turmas lideradas por este professor
                turmas_a_remover = []
                for turma in TURMAS:
                    if turma.professor.id == prof_id:
                        turmas_a_remover.append(turma)
                for t in turmas_a_remover:
                    TURMAS.remove(t)
                print(f"Sucesso: Professor '{prof.nome}' removido do sistema!")
            except ValueError:
                print("Erro: ID inválido.")
                
        elif opcao == "9":
            print("\n--- MATRICULAR ALUNO EM TURMA ---")
            if len(ALUNOS) == 0 or len(TURMAS) == 0:
                print("Erro: É necessário possuir alunos e turmas cadastradas para matricular.")
                continue
            try:
                aluno_id = int(input("Digite o ID do Aluno: "))
                aluno = buscar_aluno_por_id(aluno_id)
                if aluno is None:
                    print("Erro: Aluno não localizado.")
                    continue
                
                print("\nTurmas disponíveis:")
                for turma in TURMAS:
                    print(f"ID: {turma.id} | {turma.nome} (Prof. {turma.professor.nome})")
                    
                turma_id = int(input("Digite o ID da Turma desejada: "))
                turma = buscar_turma_por_id(turma_id)
                if turma is None:
                    print("Erro: Turma não localizada.")
                    continue
                
                turma.adicionar_aluno(aluno)
                print(f"Sucesso: Aluno '{aluno.nome}' matriculado na turma '{turma.nome}'!")
            except ValueError:
                print("Erro: Entrada inválida.")
                
        elif opcao == "10":
            break
        else:
            print("Opção inválida! Tente novamente.")


# =====================================================================
# 2. ÁREA DO PROFESSOR (LANÇAR NOTAS, FALTAS E VER RELATÓRIO)
# =====================================================================

def menu_professores():
    if len(PROFESSORES) == 0:
        print("\nErro: Nenhum professor cadastrado no sistema para simulação.")
        return
        
    print("\n--- LOGIN DO PROFESSOR ---")
    for prof in PROFESSORES:
        print(f"ID: {prof.id} | {prof.nome} ({prof.especialidade})")
        
    try:
        prof_id = int(input("Digite o ID do professor que você deseja simular: "))
        professor = buscar_professor_por_id(prof_id)
        if professor is None:
            print("Erro: Professor não localizado.")
            return
    except ValueError:
        print("Erro: ID inválido.")
        return

    # Filtra as turmas que este professor ministra
    turmas_do_prof = []
    for t in TURMAS:
        if t.professor.id == professor.id:
            turmas_do_prof.append(t)

    if len(turmas_do_prof) == 0:
        print(f"\nO professor {professor.nome} não possui nenhuma turma sob sua gerência.")
        return

    while True:
        print(f"\n================== PAINEL DO PROF. {professor.nome.upper()} ==================")
        print("Turmas Ativas:")
        for idx, t in enumerate(turmas_do_prof):
            print(f"  [{idx + 1}] Nº turma: {idx + 1} | ID da turma: {t.id} | Nome: {t.nome}")
        print("-" * 65)
        print("1. Lançar Nota para Aluno")
        print("2. Lançar Falta para Aluno")
        print("3. Visualizar Relatório de Notas da Turma")
        print("4. Matricular Aluno em uma Turma Sob sua Gerência")
        print("5. Voltar ao Menu Principal")
        print("=====================================================================")
        
        opcao = input("Selecione uma opção (1-5): ").strip()
        
        if opcao in ["1", "2", "3"]:
            # Pergunta para qual turma deseja executar a ação
            try:
                escolha_turma = int(input(f"Digite o número da turma acima (1-{len(turmas_do_prof)}): "))
                if escolha_turma < 1 or escolha_turma > len(turmas_do_prof):
                    print("Erro: Seleção de turma fora dos limites.")
                    continue
                turma_ativa = turmas_do_prof[escolha_turma - 1]
            except ValueError:
                print("Erro: Entrada numérica inválida.")
                continue

            if len(turma_ativa.alunos) == 0:
                print(f"A turma '{turma_ativa.nome}' ainda não possui nenhum aluno matriculado.")
                continue

            if opcao == "1":
                print(f"\n--- LANÇAR NOTA: {turma_ativa.nome} ---")
                for aluno in turma_ativa.alunos:
                    print(f"ID: {aluno.id} | Aluno: {aluno.nome}")
                try:
                    aluno_id = int(input("Digite o ID do Aluno para dar nota: "))
                    nota = float(input("Digite o valor da nota (0.0 a 10.0): "))
                    if nota < 0 or nota > 10:
                        print("Erro: A nota deve estar contida entre 0.0 e 10.0.")
                        continue
                    sucesso = turma_ativa.registrar_nota_aluno(aluno_id, nota)
                    if sucesso:
                        aluno_obj = buscar_aluno_por_id(aluno_id)
                        print(f"Sucesso: Nota {nota:.1f} atribuída para '{aluno_obj.nome}'!")
                    else:
                        print("Erro: Aluno não encontrado na turma ativa.")
                except ValueError:
                    print("Erro: Digite valores válidos.")

            elif opcao == "2":
                print(f"\n--- LANÇAR FALTA: {turma_ativa.nome} ---")
                print("Alunos Matriculados:")
                for aluno in turma_ativa.alunos:
                    print(f"ID: {aluno.id} | Aluno: {aluno.nome} (Faltas Atuais: {aluno.faltas})")
                try:
                    aluno_id = int(input("Digite o ID do Aluno para aplicar falta: "))
                    
                    sucesso = turma_ativa.registrar_falta_aluno(aluno_id)
                    
                except ValueError:
                    print("Erro: Entrada inválida.")

            elif opcao == "3":
                turma_ativa.gerar_relatorio_notas_professor()
                input("Clique qualquer tecla para continuar.")

        elif opcao == "4":
            print(f"\n--- MATRICULAR ALUNO EM TURMA SOB SUA GERÊNCIA ---")
            print("Selecione qual de suas turmas deseja gerenciar:")
            for idx, t in enumerate(turmas_do_prof):
                print(f"  [{idx + 1}] Nº turma: {idx + 1} | ID da turma: {t.id} | Nome: {t.nome}")
            try:
                escolha_turma = int(input(f"Número da turma (1-{len(turmas_do_prof)}): "))
                if escolha_turma < 1 or escolha_turma > len(turmas_do_prof):
                    print("Erro: Opção inválida.")
                    continue
                turma_ativa = turmas_do_prof[escolha_turma - 1]
                
                print("\nTodos os Alunos do sistema:")
                for aluno in ALUNOS:
                    print(f"ID: {aluno.id} | Aluno: {aluno.nome}")
                
                aluno_id = int(input("ID do Aluno para matricular nesta turma: "))
                aluno = buscar_aluno_por_id(aluno_id)
                if aluno is None:
                    print("Erro: Aluno não localizado.")
                    continue
                
                turma_ativa.adicionar_aluno(aluno)
                print(f"Sucesso: Aluno '{aluno.nome}' adicionado à turma '{turma_ativa.nome}'!")
            except ValueError:
                print("Erro: Entrada inválida.")

        elif opcao == "5":
            break
        else:
            print("Opção inválida! Tente novamente.")


# =====================================================================
# 3. ÁREA DO ALUNO (BOLETIM GERAL E RELATÓRIO INDIVIDUAL DE DISCIPLINA)
# =====================================================================

def menu_alunos():
    if len(ALUNOS) == 0:
        print("\nErro: Nenhum aluno cadastrado no sistema para simulação.")
        return
        
    print("\n--- LOGIN DO ALUNO ---")
    for aluno in ALUNOS:
        print(f"ID: {aluno.id} | {aluno.nome}")
        
    try:
        aluno_id = int(input("Digite o ID do aluno que deseja simular: "))
        aluno_ativo = buscar_aluno_por_id(aluno_id)
        if aluno_ativo is None:
            print("Erro: Aluno não localizado.")
            return
    except ValueError:
        print("Erro: ID inválido.")
        return

    # Descobre em quais turmas o aluno está matriculado
    turmas_do_aluno = []
    for t in TURMAS:
        for a in t.alunos:
            if a.id == aluno_ativo.id:
                turmas_do_aluno.append(t)
                break

    while True:
        print(f"\n================== PAINEL DO ALUNO: {aluno_ativo.nome.upper()} ==================")
        print("1. Ver Notas e Relatório Individual de uma Disciplina")
        print("2. Ver Boletim Geral de Todas as Disciplinas")
        print("3. Voltar ao Menu Principal")
        print("=========================================================================")
        
        opcao = input("Selecione uma opção (1-3): ").strip()
        
        if opcao == "1":
            print(f"\n--- RELATÓRIO INDIVIDUAL DE DISCIPLINA ---")
            if len(turmas_do_aluno) == 0:
                print("Você não está matriculado em nenhuma disciplina.")
                continue
                
            print("Selecione a disciplina:")
            for idx, t in enumerate(turmas_do_aluno):
                print(f"  [{idx + 1}] {t.nome} (Prof. {t.professor.nome})")
                
            try:
                escolha = int(input("Digite o número correspondente: "))
                if escolha < 1 or escolha > len(turmas_do_aluno):
                    print("Erro: Opção inválida.")
                    continue
                turma_sel = turmas_do_aluno[escolha - 1]
                
                notas = aluno_ativo.obter_notas_turma(turma_sel.id)
                notas_str = ""
                for n in notas:
                    notas_str += f"{n:.1f}  "
                if not notas_str:
                    notas_str = "Sem notas lançadas"
                
                media_calculada_com_pesos = aluno_ativo.calcular_media_individual_aluno(turma_sel.id)
                
                print(f"\nDisciplina: {turma_sel.nome}")
                print(f"Professor: {turma_sel.professor.nome}")
                print(f"Suas Notas: [ {notas_str} ]")
                print(f"Média: {media_calculada_com_pesos:.2f}")
                print("-" * 55)
            except ValueError:
                print("Erro: Entrada numérica inválida.")
                
        elif opcao == "2":
            aluno_ativo.exibir_boletim_geral(TURMAS)

            
        elif opcao == "3":
            break
        else:
            print("Opção inválida! Tente novamente.")


# =====================================================================
# 4. LOOP DE EXECUÇÃO PRINCIPAL
# =====================================================================

def main():
    global ALUNOS, PROFESSORES, TURMAS
    
    # Carrega dados padrão de teste inicial
    ALUNOS, PROFESSORES, TURMAS = carregar_dados_sistema()
    
    while True:
        print("\n" + "=" * 65)
        print("      SISTEMA DE GERENCIAMENTO ESCOLAR")
        print("=" * 65)
        print("Selecione o perfil que deseja simular:")
        print("1. Área Administrativa")
        print("2. Área do Professor (Lançamento de Notas, Faltas e Relatórios)")
        print("3. Área do Aluno (Visualização de Notas e Boletim Geral)")
        print("4. Sair do SISTEMA DE GERENCIAMENTO ESCOLAR")
        print("=" * 65)
        
        opcao = input("Selecione uma opção (1-4): ").strip()
        
        if opcao == "1":
            menu_administracao()
        elif opcao == "2":
            menu_professores()
        elif opcao == "3":
            menu_alunos()
        elif opcao == "4":
            print("\nFinalizando execução do SISTEMA DE GERENCIAMENTO ESCOLAR!")
            sys.exit(0)
        else:
            print("Opção inválida! Selecione um número de 1 a 4.")

if __name__ == "__main__":
    main()

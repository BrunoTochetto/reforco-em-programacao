# =====================================================================
# SISTEMA DE GERENCIAMENTO ESCOLAR - MODELO DO ALUNO
# =====================================================================

class Aluno:
    id = 104 # Utilizado esse número por motivos de teste, o MOCK acaba em 104, então usaremos 104 em diante.

    def __init__(self, aluno_id, nome):
        self.id = aluno_id
        self.nome = nome
        self.faltas = 0
        # Dicionário para armazenar notas por ID da Turma
        # Exemplo: {1: [8.5, 7.0], 2: [9.0, 10.0]}
        self.notas_por_turma = {}

    def adicionar_nota(self, turma_id, nota):
        if turma_id not in self.notas_por_turma:
            self.notas_por_turma[turma_id] = []
        self.notas_por_turma[turma_id].append(nota)

    def obter_notas_turma(self, turma_id):
        if turma_id in self.notas_por_turma:
            return self.notas_por_turma[turma_id]
        return []

    def calcular_media_individual_aluno(self, turma_id):
        """
        Calcula a média de notas do aluno em uma turma específica.
        """
        notas = self.obter_notas_turma(turma_id)
        if len(notas) == 0:
            return 0.0

        if len(notas) >= 2:
            soma_com_pesos = (notas[0] * 1.5) + (notas[1] * 0.5)
            for i in range(2, len(notas)):
                soma_com_pesos += notas[i]
            return soma_com_pesos / len(notas)
        
        # Se tiver apenas 1 nota, retorna a nota normal dividido por 1
        return notas[0]

    def obter_media_real_correta(self, turma_id):
        """
        Método correto (auxiliar para comparação de depuração)
        """
        notas = self.obter_notas_turma(turma_id)
        if len(notas) == 0:
            return 0.0
        soma = 0.0
        for nota in notas:
            soma += nota
        return soma / len(notas)


    def exibir_boletim_geral(self, lista_todas_turmas):
        """
        Exibe a média do aluno em todas as disciplinas que ele está matriculado.
        """
        # Filtra apenas as turmas em que este aluno está matriculado
        turmas_matriculado = []
        for turma in lista_todas_turmas:
            for aluno_matriculado in turma.alunos:
                if aluno_matriculado.id == self.id:
                    turmas_matriculado.append(turma)
                    break

        if len(turmas_matriculado) == 0:
            print(f"O aluno {self.nome} não está matriculado em nenhuma turma.")
            return


        medias = []
        for turma in turmas_matriculado:
            notas = self.obter_notas_turma(turma.id)
            if len(notas) > 0:
                soma = 0.0
                for n in notas:
                    soma += n
                media = soma / len(notas)
            else:
                media = 0.0
            medias.append(media)

        def obter_nome_turma(t):
            return t.nome

        turmas_ordenadas_alfabeticamente = sorted(turmas_matriculado, key=obter_nome_turma)

        print(f"\n=================== BOLETIM GERAL DE {self.nome.upper()} ===================")
        print(f"Faltas Totais: {self.faltas}")
        print("-" * 65)
        print(f"{'DISCIPLINA':<35} | {'MÉDIA OBTIDA':<15}")
        print("-" * 65)

        for i in range(len(turmas_ordenadas_alfabeticamente)):
            turma_nome = turmas_ordenadas_alfabeticamente[i].nome
            media = medias[i]
            print(f"{turma_nome:<35} | {media:<15.2f}")
        print("=====================================================================")


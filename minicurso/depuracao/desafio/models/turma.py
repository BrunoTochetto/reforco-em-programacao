# =====================================================================
# SISTEMA DE GERENCIAMENTO ESCOLAR - MODELO DA TURMA
# =====================================================================

class Turma:
    def __init__(self, turma_id, nome, professor):
        self.id = turma_id
        self.nome = nome
        self.professor = professor
        self.alunos = []

    def adicionar_aluno(self, aluno):
        # Evita duplicidade de matrícula na mesma turma
        ja_matriculado = False
        for a in self.alunos:
            if a.id == aluno.id:
                ja_matriculado = True
                break
        if not ja_matriculado:
            self.alunos.append(aluno)

    def registrar_nota_aluno(self, aluno_id, nota):
        for aluno in self.alunos:
            if aluno.id == aluno_id:
                aluno.adicionar_nota(self.id, nota)
                return True
        return False

    def registrar_falta_aluno(self, aluno):
        """
        Registra uma falta para o aluno correspondente.
        """
        # PARA FAZER -> Implementar falta
        if len(self.alunos) > 0:
            self.alunos[0].faltas += 1

            return True
        return False

    def gerar_relatorio_notas_professor(self):
        """
        Gera um relatório de notas da turma para visualização do professor.
        """
        print(f"\n=== RELATÓRIO DE NOTAS DA DISCIPLINA: {self.nome} ===")
        print(f"Professor: {self.professor.nome}")
        print("-" * 80)
        print(f"{'ALUNO':<20} | {'NOTAS LANÇADAS':<25} | {'FALTAS':<8} | {'MÉDIA DA DISCIPLINA':<15}")
        print("-" * 80)

        for aluno in self.alunos:
            notas = aluno.obter_notas_turma(self.id)
            
            # Formatação simples das notas para exibição
            notas_str = ""
            for n in notas:
                notas_str += f"{n:.1f}  "
            if not notas_str:
                notas_str = "Sem notas"

            if len(notas) > 0:
                media_calculada = notas[0]
            else:
                media_calculada = 0.0

            print(f"{aluno.nome:<20} | {notas_str:<25} | {aluno.faltas:<8} | {media_calculada:<15.2f}")
        print("-" * 80)

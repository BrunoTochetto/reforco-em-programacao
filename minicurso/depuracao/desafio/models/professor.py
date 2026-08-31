# =====================================================================
# SISTEMA DE GERENCIAMENTO ESCOLAR - MODELO DO PROFESSOR
# =====================================================================

class Professor:
    id = 204 # Utilizado esse número por motivos de teste, o MOCK acaba em 204, então usaremos 204 em diante.

    def __init__(self, professor_id, nome, especialidade):
        self.id = professor_id
        self.nome = nome
        self.especialidade = especialidade

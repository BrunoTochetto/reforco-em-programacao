# -*- coding: utf-8 -*-
# =====================================================================
# LAB DE DECURAÇÃO - DESAFIO 2: BUSCA DIVIDIDA AO MEIO (BISECTION)
# Curso de Informática para Internet (Ensino Médio Técnico)
# Baseado nas metodologias do MIT Reading 13
# =====================================================================

"""
TEORIA: BUSCA DIVIDIDA AO MEIO (BISECTION / BINARY SEARCH DE BUGS)
Quando temos um fluxo de processamento com muitas etapas sequenciais (ex: tratamento de dados,
comunicações web ou pipelines), rastrear linha por linha é ineficiente.

A técnica consiste em dividir as etapas de processamento exatamente ao meio:
1. Colocamos um breakpoint() ou print de inspeção no MEIO do fluxo (ex: Etapa 3 de um fluxo de 6).
2. Se o dado estiver CORRETO no meio, sabemos que a primeira metade está livre de erros.
   O bug deve estar entre a Etapa 4 e 6.
3. Se o dado estiver INCORRETO no meio, o bug ocorreu logo nas primeiras etapas (Etapa 1 a 3).
4. Dividimos a metade suspeita novamente ao meio, localizando o bug em tempo recorde!
"""

# =====================================================================
# PIPELINE DE TRATAMENTO DE TEXTO WEB (VERSÃO COM BUG)
# =====================================================================
def pipeline_tratamento_errado(entrada_usuario):
    """
    Simula o processamento sequencial de um comentário enviado por formulário web.
    O objetivo é limpar espaços, remover HTML perigoso, converter para minúsculas, 
    censurar palavras impróprias, adicionar quebras de linha e validar o tamanho.
    """
    # Etapa 1: Remover espaços extras nas pontas
    texto = entrada_usuario.strip()
    
    # Etapa 2: Remover tags HTML perigosas para evitar ataques XSS
    texto = texto.replace("<script>", "").replace("</script>", "")
    
    # Etapa 3: Converter todo o texto para minúsculas
    # BUG SILENCIOSO: O programador queria usar texto.lower(), mas usou 'texto.title()' por engano!
    # Isso vai transformar "Censurado" em "Censurado" e bagunçar a censura exata da Etapa 4.
    texto = texto.title()
    
    # --- METADE DO CAMINHO (Ponto ideal para o Breakpoint) ---
    
    # Etapa 4: Censurar palavra inadequada ("bobao")
    texto = texto.replace("bobao", "[censurado]")
    
    # Etapa 5: Substituir quebras de texto por tag <br> para exibição em HTML
    texto = texto.replace("\n", "<br>")
    
    # Etapa 6: Cortar texto se passar do limite máximo de 100 caracteres
    if len(texto) > 100:
        texto = texto[:97] + "..."
        
    return texto


# =====================================================================
# PIPELINE CORRIGIDO (VERSÃO CERTA)
# =====================================================================
def pipeline_tratamento_certo(entrada_usuario):
    """
    Versão corrigida após aplicar a busca dividida ao meio e achar a falha na Etapa 3.
    """
    texto = entrada_usuario.strip()
    texto = texto.replace("<script>", "").replace("</script>", "")
    
    # CORREÇÃO: Usando lower() para que a censura da etapa seguinte encontre a palavra em minúsculas
    texto = texto.lower() 
    
    texto = texto.replace("bobao", "[censurado]")
    texto = texto.replace("\n", "<br>")
    
    if len(texto) > 100:
        texto = texto[:97] + "..."
        
    return texto


# =====================================================================
# ÁREA DE EXECUÇÃO DO ALUNO
# =====================================================================
if __name__ == "__main__":
    print("-" * 75)
    print("DEMONSTRAÇÃO: BUSCA DIVIDIDA AO MEIO")
    print("-" * 75)
    
    comentario_web = "  Aquele desenvolvedor é um bobao! \n Veja o meu site. "
    print(f"Texto original enviado pelo formulário:\n'{comentario_web}'\n")
    
    # Esperado: A palavra "bobao" deve ser censurada e o texto ficar limpo em minúsculas.
    # Resultado Esperado: "aquele desenvolvedor é um [censurado]!<br> veja o meu site."
    
    print("Roda o pipeline com bug:")
    resultado_errado = pipeline_tratamento_errado(comentario_web)
    print(f"Resultado Obtido: '{resultado_errado}'")
    print("SINTOMA: A palavra 'bobao' NÃO FOI CENSURADA! Por quê?")
    
    print("\nComo aplicar a Busca Dividida ao Meio:")
    print("1. Insira um 'breakpoint()' no meio da função 'pipeline_tratamento_errado' (após a Etapa 3).")
    print("2. Rode o script. Quando o programa pausar, verifique o valor da variável 'texto' usando 'p texto'.")
    print("3. Se o texto estiver com letras maiúsculas em cada palavra ('Aquele Desenvolvedor...'),")
    print("   você saberá que o erro está na primeira metade do pipeline (Etapa 1, 2 ou 3)!")
    print("4. Olhando as Etapas 1, 2 e 3, fica claro que a Etapa 3 (title()) alterou o estado incorretamente.")
    
    # Para praticar, descomente o breakpoint abaixo para ver como seria parar no meio:
    # breakpoint()
    
    print("\n" + "-" * 75)
    print("PIPELINE CORRIGIDO")
    print("-" * 75)
    resultado_certo = pipeline_tratamento_certo(comentario_web)
    print(f"Resultado Corrigido: '{resultado_certo}'")
    print("-" * 75)

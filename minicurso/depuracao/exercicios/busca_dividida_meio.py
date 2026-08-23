# =====================================================================
# Minicurso de Informática para Internet - IFC Concórdia
# Semana de Ensino Pesquisa e Extensão (SEPE)
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
def pipeline_tratamento_original(entrada_usuario):
    """
    Simula o processamento sequencial de um comentário enviado por formulário web.
    O objetivo é limpar espaços, remover HTML perigoso, converter para minúsculas, 
    censurar palavras impróprias, adicionar quebras de linha e validar o tamanho.
    """
    # Etapa 1: Remover espaços extras nas pontas
    texto = entrada_usuario.strip()
    
    # Etapa 2: Remover tags HTML perigosas para evitar ataques XSS
    texto = texto.replace("<script>", "").replace("</script>", "")
    
    # Etapa 3: Converter todo o texto para minúsculas para que a censura da etapa seguinte encontre a palavra em minúsculo
    texto = texto.title()
    
    # Etapa 4: Censurar palavra inadequada ("bobao")
    texto = texto.replace("bobao", "[censurado]")
    
    # Etapa 5: Substituir quebras de texto por tag <br> para exibição em HTML
    texto = texto.replace("\n", "<br>")
    
    # Etapa 6: Cortar texto se passar do limite máximo de 100 caracteres
    if len(texto) > 100:
        texto = texto[:97] + "..."
        
    return texto



comentario_web = "  Aquele desenvolvedor é um bobao! \n Veja o meu site. "
print(f"Texto original enviado pelo formulário:\n'{comentario_web}'\n")

# Esperado: A palavra "bobao" deve ser censurada e o texto ficar limpo em minúsculas.
# Resultado Esperado: "aquele desenvolvedor é um [censurado]!<br> veja o meu site."

resultado_errado = pipeline_tratamento_original(comentario_web)
print(f"Resultado Obtido: '{resultado_errado}'")
# SINTOMA: A palavra 'bobao' NÃO FOI CENSURADA! Por quê?"

#Como aplicar a Busca Dividida ao Meio:
#1. Insira um 'breakpoint()' no meio da função 'pipeline_tratamento_original'.
#2. Rode o script. Quando o programa pausar, verifique o valor da variável 'texto'.
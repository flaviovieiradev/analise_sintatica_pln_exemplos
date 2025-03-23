import spacy
import pandas as pd
from spacy import displacy

# Carrega o modelo em português do spaCy
# 'pt_core_news_sm' é um modelo pequeno para português
# Se estiver usando pela primeira vez, instale com: python -m spacy download pt_core_news_sm
nlp = spacy.load('pt_core_news_sm')

# Define a frase que será analisada
frase = "O estudante inteligente leu um livro sobre linguística no final de semana."

# Processa a frase com o pipeline do spaCy
# Isso executa tokenização, POS tagging, parsing de dependências, etc.
doc = nlp(frase)

# Cria um DataFrame para visualizar as informações de maneira estruturada
# Isso facilita entender as relações entre as palavras
dados = []
for token in doc:
    # Para cada token, coletamos informações relevantes
    dados.append({
        'Índice': token.i,                   # Posição da palavra na frase
        'Palavra': token.text,               # Texto da palavra
        'Lema': token.lemma_,                # Forma base/dicionário da palavra
        'POS': token.pos_,                   # Classe gramatical (Part of Speech)
        'TAG': token.tag_,                   # Tag morfológica mais detalhada
        'Dependência': token.dep_,           # Relação de dependência
        'Índice_Pai': token.head.i,          # Índice da palavra "pai"
        'Palavra_Pai': token.head.text,      # Texto da palavra "pai"
        'Filhos': [child.text for child in token.children]  # Palavras que dependem desta
    })

# Cria e exibe o DataFrame formatado
df = pd.DataFrame(dados)
print("\n=== ANÁLISE DETALHADA DE DEPENDÊNCIAS ===\n")
print(df[['Índice', 'Palavra', 'POS', 'Dependência', 'Palavra_Pai', 'Filhos']])
print("\n")

# Imprime a árvore de dependências em formato textual
# Mostra cada palavra seguida da relação e de quem ela depende
print("=== ÁRVORE DE DEPENDÊNCIAS (FORMATO TEXTUAL) ===\n")
for token in doc:
    # Formata a saída como: palavra --relação--> palavra_pai
    print(f"{token.text} --{token.dep_}--> {token.head.text}")

# Função para gerar visualização da árvore em HTML
# Esta função permite salvar a representação visual da árvore
def salvar_visualizacao(doc, arquivo="arvore_dependencias.html"):
    """Salva a visualização da árvore de dependências em um arquivo HTML."""
    html = displacy.render(doc, style="dep", page=True, options={"compact": True})
    
    # Adiciona CSS para melhorar a visualização
    css = """
    <style>
    body { 
        font-family: Arial, sans-serif;
        margin: 20px;
    }
    h2 {
        color: #333;
        border-bottom: 1px solid #ccc;
        padding-bottom: 10px;
    }
    </style>
    """
    html = html.replace("</head>", f"{css}</head>")
    html = html.replace("<body>", "<body><h2>Árvore de Dependências</h2>")
    
    # Salva no arquivo
    with open(arquivo, "w", encoding="utf-8") as f:
        f.write(html)
    print(f"\nVisualizacão salva no arquivo: {arquivo}")

# Salva a visualização em HTML
salvar_visualizacao(doc)

# Para visualizar a árvore diretamente no notebook Jupyter (se estiver usando um)
# Descomente a linha abaixo:
# displacy.render(doc, style="dep", jupyter=True)

print("\n=== ANÁLISE SIMPLES DA ESTRUTURA DA FRASE ===\n")

# Extrai sujeitos, verbos e objetos para análise básica da estrutura
sujeitos = [token.text for token in doc if token.dep_ == 'nsubj']
verbos = [token.text for token in doc if token.pos_ == 'VERB']
objetos = [token.text for token in doc if token.dep_ == 'obj']

print(f"Sujeito(s): {sujeitos}")
print(f"Verbo(s): {verbos}")
print(f"Objeto(s): {objetos}")

# Encontra a raiz da frase (geralmente o verbo principal)
raiz = [token for token in doc if token.head == token][0]
print(f"\nRaiz da frase: {raiz.text} ({raiz.pos_})")

# Mostra exemplos de diferentes tipos de relações na frase
print("\nExemplos de relações encontradas:")
for tipo_rel in set(token.dep_ for token in doc):
    palavras = [token.text for token in doc if token.dep_ == tipo_rel]
    print(f"- {tipo_rel}: {', '.join(palavras)}")

print("\nEsta análise mostra como as palavras se relacionam diretamente umas com as outras na estrutura sintática da frase.")
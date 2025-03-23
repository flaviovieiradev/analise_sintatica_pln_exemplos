# Código para Análise de Constituintes em Python usando NLTK

# Importando as bibliotecas necessárias
import nltk
from nltk import CFG  # Context-Free Grammar (Gramática Livre de Contexto)
from nltk.parse.chart import ChartParser  # Parser para análise sintática

# Antes de executar este código, instale o NLTK com:
# pip install nltk

# Baixar recursos necessários do NLTK (execute apenas na primeira vez)
# O módulo 'punkt' é usado para tokenização (separação da frase em palavras)
nltk.download('punkt')

def definir_gramatica():
    """
    Define uma gramática livre de contexto (CFG) em português.
    """
    return CFG.fromstring("""
        S -> NP VP
        NP -> Det N | Det N PP | 'Maria' | 'João' | 'palmeiras' | 'mundial'
        VP -> V NP | V NP PP | Adv V NP
        PP -> P NP
        Det -> 'o' | 'a' | 'um' | 'uma' | 'O'
        N -> 'menino' | 'menina' | 'bola' | 'parque' | 'palmeiras' | 'mundial'
        V -> 'chutou' | 'jogou' | 'viu' | 'tem'
        P -> 'com' | 'no' | 'na'
        Adv -> 'não'
    """)

def analisar_frase(parser, sentence):
    """
    Realiza a análise sintática da frase e exibe as árvores sintáticas possíveis.
    """
    print("Analisando a frase:", " ".join(sentence))
    print("\nÁrvore(s) sintática(s) possível(is):")

    encontrou_arvore = False
    for i, tree in enumerate(parser.parse(sentence)):
        encontrou_arvore = True
        print(f"\nÁrvore #{i + 1}:")
        print(tree)
        # Visualização gráfica da árvore (descomente para usar)
        # tree.draw()
        print("\nVisualização em texto indentado:")
        tree.pretty_print()

    if not encontrou_arvore:
        print("Nenhuma árvore sintática encontrada para a frase fornecida.")

def main():
    # Definir a gramática
    grammar = definir_gramatica()

    # Criar o parser usando a gramática definida
    parser = ChartParser(grammar)

    # Definir a frase a ser analisada e sua tokenização
    sentence = "O palmeiras não tem mundial".split()

    # Analisar a frase
    analisar_frase(parser, sentence)

if __name__ == "__main__":
    main()

"""
Para executar este código, você precisa:

1. Instalar o Python (recomendado Python 3.7 ou superior)
   - Download: https://www.python.org/downloads/

2. Instalar o NLTK via pip:
   - Abra o terminal/prompt de comando
   - Execute: pip install nltk

3. (Opcional) Para a visualização gráfica, pode ser necessário instalar:
   - tkinter: geralmente já vem com Python, mas caso não esteja disponível:
     - No Linux: sudo apt-get install python3-tk
     - No Windows: normalmente já vem instalado com Python
     - No macOS: brew install python-tk

4. Na primeira execução, o código baixará automaticamente o pacote 'punkt' necessário.
"""
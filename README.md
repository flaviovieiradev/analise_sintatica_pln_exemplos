# Análise Sintática de Frases em Português

Este projeto contém exemplos de análise sintática de frases em português utilizando as bibliotecas `spaCy` e `NLTK` em Python.

## Estrutura do Projeto

- `exemplo_arvore_dependencia.py`: Script que realiza a análise de dependências de uma frase em português utilizando o `spaCy`.
- `ex_analise_constituinte.py`: Script que realiza a análise de constituintes de uma frase em português utilizando o `NLTK`.

## Requisitos

- Python 3.7 ou superior
- Bibliotecas Python:
  - `spacy`
  - `pandas`
  - `nltk`

## Instalação

1. Clone o repositório:
    ```sh
    git clone https://github.com/flaviovieiradev/analise_sintatica_pln_exemplos.git
    cd apresentacao-analise-sintatica-pln
    ```

2. Instale as dependências:
    ```sh
    pip install spacy pandas nltk
    ```

3. Baixe o modelo de linguagem em português do `spaCy`:
    ```sh
    python -m spacy download pt_core_news_sm
    ```

4. Baixe os recursos necessários do `NLTK`:
    ```sh
    python -c "import nltk; nltk.download('punkt')"
    ```

## Uso

### Árvore de Dependências

Para executar a análise de dependências, execute o script `exemplo_arvore_dependencia.py`:

### Análise Constituinte

Para executar a análise de dependências, execute o script `exemplo_analise_constituinte.py`:

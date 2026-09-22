# Comandos do terminal

Rodei tudo no PowerShell com o venv ativado.

```
C:\Users\gusta\venv\Scripts\Activate.ps1
```

## Interpretador do Python

```
python
```

```python
print("Card 7 - interpretador do Python")   # testo se abriu certo
2 ** 10                                     
exit()                                      # volto pro terminal
```

Nada fica salvo aqui, entao so serve pra teste rapido.

## Rodando um script

Crio um arquivo `test_script.py` com uma linha:

```python
print("hello viewers")
```

E rodo direto pelo terminal sem abrir o interpretador:

```
python test_script.py
```

Isso já fica salvo normalmente mas perco a parte interativa pra mudar qualquer coisa
preciso editar o arquivo e rodar de novo do zero.

## IPython

```
pip install ipython
ipython
```

```python
import pand   # digito ate aqui e aperto Tab
```

O Tab abre a lista e sugere `pandas` e `pandocfilters`.
uma coisa legal que o codigo ja sai colorido 

## Subir o Jupyter Notebook

```
pip install notebook numpy matplotlib
jupyter notebook
```

Sobe um servidor local na porta 8888 e abre o navegador em `localhost:8888`.

## Subir o Jupyter Lab

```
pip install jupyterlab
jupyter lab
```

Antes derrubo o servidor anterior com `Ctrl + C`, senao a porta fica ocupada.

## Reproduzir o erro de ordem de execução

No Jupyter Lab, com o kernel recem reiniciado:

1. rodo primeiro a celula do grafico pulando a do import
2. aparece `NameError: name 'np' is not defined`
3. a celula do import continua com `[ ]` e a do grafico ja marca `[1]`

O numero entre colchetes mostra a ordem em que eu rodei e nao a posicao no arquivo.
Por isso uso Kernel > Restart & Run All antes de entregar.

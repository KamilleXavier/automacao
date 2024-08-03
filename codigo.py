# Passo a passo do projeto

# 1. Abrir o sistema da empresa
    # https://dlp.hashtagtreinamentos.com/python/intensivao/login

# para instalar: pip instal pyautogui
import pyautogui
import time
import webbrowser

pyautogui.PAUSE = 0.5

#   ---COMANDOS PYAUTOGUI---
# pyautogui.click -> clicar com o mouse
# pyautogui.write -> escrever um texto
# pyautogui.press -> pressionar uma tecla do teclado
# pyautogui.hotkey -> apertar um conjunto de teclas (Ctrl+C, Ctrl+V, Alt Tab) 

# abrir navegador (Chrome)
pyautogui.write("google")
pyautogui.press("enter")

# entrar no site do sistema
webbrowser.open("https://dlp.hashtagtreinamentos.com/python/intensivao/login")
pyautogui.write("https://dlp.hashtagtreinamentos.com/python/intensivao/login")
pyautogui.press("enter")

# aqui pode ser que ele demore a alguns segundos para carregar o site
time.sleep(3)

# 2. Fazer login
pyautogui.click(x=875, y=434)
pyautogui.write("kamillexavier239@gmail.com")
pyautogui.press("tab") #passou para o proximo campo
pyautogui.write("senha")
pyautogui.press("tab") #passou para o proximo campo 
pyautogui.press("enter")

# 3. Abrir/Importar a base de dados de produtos para cadastrar
# pip install pandas numy openpyxl
import pandas as pd

tabela = pd.read_csv("produtos.csv")
# SIMBOLO DE = SIGNIFICA RECEBE
# Tabula é um pacote do python que transforma pdf em pandas
print(tabela)

# 4. Cadastrar um produtos
#str -> string (que significa texto)

for linha in tabela.index:
    codigo = str(tabela.loc[linha, "codigo"])
    # clicar no campo do codigo do produto
    pyautogui.click(x=740, y=327)

    # preencher o codigo
    pyautogui.write(codigo)

    #passar para o proximo campo
    pyautogui.press("tab")

    #marca
    pyautogui.write(str(tabela.loc[linha, "marca"]))
    #passar para o proximo campo
    pyautogui.press("tab")

    #tipo
    pyautogui.write(str(tabela.loc[linha, "tipo"]))
    #passar para o proximo campo
    pyautogui.press("tab")

    #categoria
    pyautogui.write(str(tabela.loc[linha, "categoria"]))
    #passar para o proximo campo
    pyautogui.press("tab")

    #preço
    pyautogui.write(str(tabela.loc[linha, "preco_unitario"]))
    #passar para o proximo campo
    pyautogui.press("tab")

    #custo
    pyautogui.write(str(tabela.loc[linha, "custo"]))
    #passar para o proximo campo
    pyautogui.press("tab")

    #obs 
    obs = str(tabela.loc[linha, "obs"])
    if obs != "nan":
        pyautogui.write(obs)

    #diferente no python significa !=
    #passar para o proximo campo
    pyautogui.press("tab")
    # apertar botão]
    pyautogui.press("enter")
    pyautogui.scroll(5000)

# 5. Repetir isso tudo até acabar a lista TEPH0002720   Philco  TCL Televisao   
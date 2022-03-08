# -*- coding: utf-8 -*-
"""
Created on Fri Feb  4 11:51:41 2022

@author: eduar
passo 1: definir o codigo em uma função
passo 2: abrir o Tk() e o mainloop()





"""
import requests
from tkinter import *


def pegar_cotacoes():
    requisicao = requests.get("https://economia.awesomeapi.com.br/last/USD-BRL,EUR-BRL,BTC-BRL")

    requisicao_dic = requisicao.json()

    cotacao_dolar = requisicao_dic['USDBRL']['bid']
    cotacao_euro = requisicao_dic['EURBRL']['bid']
    cotacao_btc = requisicao_dic['BTCBRL']['bid']

    texto = f'''
    Dólar: {cotacao_dolar}
    Euro: {cotacao_euro}
    BTC: {cotacao_btc}'''

    texto_cot["text"] = texto



janela = Tk()
janela.title("Cotação moedas")

texto_orientacao = Label(janela, text="Clique no botão para ver as cotações das moedas" )
texto_orientacao.grid(column=0,row =0,padx = 10, pady = 10)

botao = Button(janela, text="Buscar cotações",command =pegar_cotacoes)
botao.grid(column = 0, row = 1,padx = 20, pady = 20)

texto_cot = Label(janela,text="")
texto_cot.grid(column = 0, row = 2, padx= 30, pady = 30)


janela.mainloop() 
from tkinter import *
from tkinter import ttk
from Buscador_cotação import pegar_cotacao

moedas_codigo = ['USD','EUR', 'BTC']

# criar uma lógica que calcule a conversão
def calcular_conversao():
    entry_info = entry_valor.get()
    combobox_info = combobox_moeda_origem.get()

    if combobox_info == 'USD':
        conversao = float(pegar_cotacao('USD')) * float(entry_info)
        texto = f'O resultado da conversão é de R${conversao:,.2f}'
        resultado['text'] = texto
    elif combobox_info == 'EUR':
        conversao = float(pegar_cotacao('EUR')) * float(entry_info)
        texto = f'O resultado da conversão é de R${conversao:,.2f}'
        resultado['text'] = texto
    else:
        conversao = float(pegar_cotacao('BTC')) * float(entry_info)
        texto = f'O resultado da conversão é de R${conversao:,.2f}'
        resultado['text'] = texto

# criar a janela
janela = Tk()
janela.title('Coversor de moeda')
janela.geometry('380x160')

campo_valor = Label(janela, text='Insira o valor que deseja converter')
campo_valor.grid(column=0, row=1, padx=10, pady=10, sticky='nswe', columnspan=2)

entry_valor = Entry()
entry_valor.grid(column=2, row=1, padx=10, pady=10, sticky='nswe', columnspan=2)

origem = Label(janela, text='Selecione a origem da moeda')
origem.grid(column=0, row=3, padx=10, pady=10, sticky='nswe', columnspan=2)
combobox_moeda_origem = ttk.Combobox(values=moedas_codigo)
combobox_moeda_origem.grid(column=2, row=3, padx=10, pady=10, sticky='nswe', columnspan=2)

botao = Button(text='Calcular conversão', command=calcular_conversao)
botao.grid(column=0, row=5, padx=10, pady=10, sticky='nswe', columnspan=4)

resultado = Label(janela, text='')
resultado.grid(column=0, row=6, padx=10, pady=10, columnspan=4)

janela.mainloop()

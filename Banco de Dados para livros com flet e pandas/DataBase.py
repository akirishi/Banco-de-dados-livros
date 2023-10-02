import pandas as pd

PATH = "python\Banco de Dados para livros com flet e pandas\Livros.xlsx"
DF = pd.read_excel(PATH)

def add_book(
    nome="", editora="", tipo="", ano="", autor="", n_pag=0, valor=0.0, lido=''
):
    nova_linha = DF.loc[DF.shape[0]] = [
        DF.shape[0] + 1,
        nome,
        editora,
        tipo,
        ano,
        autor,
        n_pag,
        valor,
        lido,
    ]

def save():
    DF.to_excel(PATH, index=False)
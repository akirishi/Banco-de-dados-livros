import flet as ft
import DataBase


def main(app: ft.Page):
    titulo = ft.Text("Livros", size=50, color=ft.colors.BLACK)
    app.add(titulo)

    def abrir_popup_add_livro(e):
        app.dialog = popup_add_livro
        popup_add_livro.open = True
        app.update()

    def add_livro(e):
        nome = nome_livro.value
        editora = edit_livro.value
        tipo = tipo_livro.value
        ano = ano_livro.value
        autor = autor_livro.value
        pags = n_pag_livro.value
        preco = valor_livro.value
        lido = lido_livro.value

        DataBase.add_book(nome, editora, tipo, ano, autor, pags, preco, lido)
        DataBase.save()
        popup_add_livro.open = False
        ler_tabela(e)
        app.update()

    # Mostrar os dados dos livros
    # proposta:
    # Criar uma lista de colunas que mostre as infos dos livros da tabela

    col_nome = ft.Column()
    col_edit = ft.Column()
    col_tipo = ft.Column()
    col_ano = ft.Column()
    col_autor = ft.Column()
    col_pags = ft.Column()
    col_valor = ft.Column()
    col_lido = ft.Column()

    def ler_tabela(e=None):
        col_nome.controls.append(ft.Text("Nome do Livro:"))
        col_edit.controls.append(ft.Text("Editora:"))
        col_tipo.controls.append(ft.Text("Genêros do Livro:"))
        col_ano.controls.append(ft.Text("Ano de Lançamento:"))
        col_autor.controls.append(ft.Text("Autor(a):"))
        col_pags.controls.append(ft.Text("Nº de paginas:"))
        col_valor.controls.append(ft.Text("Valor Pago:"))
        col_lido.controls.append(ft.Text("Lido?:"))
        for nome in list(DataBase.DF["Nome"]):
            col_nome.controls.append(ft.Text(nome))
        for editora in list(DataBase.DF["Editora"]):
            col_edit.controls.append(ft.Text(editora))
        for tipo in list(DataBase.DF["Tipo"]):
            col_tipo.controls.append(ft.Text(tipo))
        for ano in list(DataBase.DF["Ano_lancamento"]):
            col_ano.controls.append(ft.Text(ano))
        for autor in list(DataBase.DF["Autor"]):
            col_autor.controls.append(ft.Text(autor))
        for pags in list(DataBase.DF["N_Paginas"]):
            col_pags.controls.append(ft.Text(pags))
        for valor in list(DataBase.DF["Valor_pago"]):
            col_valor.controls.append(ft.Text(valor))
        for lido in list(DataBase.DF["Lido"]):
            col_lido.controls.append(ft.Text(lido))
        if e != None:
            col_nome.controls.clear()
            col_edit.controls.clear()
            col_tipo.controls.clear()
            col_ano.controls.clear()
            col_autor.controls.clear()
            col_pags.controls.clear()
            col_valor.controls.clear()
            col_lido.controls.clear()
            ler_tabela()

        app.update()

    ler_tabela()
    infos = [
        col_nome,
        col_edit,
        col_tipo,
        col_ano,
        col_autor,
        col_pags,
        col_valor,
        col_lido,
    ]

    app.add(ft.Row(infos))

    botao_add_livro = ft.ElevatedButton(
        "Adicionar Livro", on_click=abrir_popup_add_livro
    )
    botao_atualizar_dados = ft.ElevatedButton(
        "atualizar dados", on_click=ler_tabela
    )

    nome_livro = ft.TextField(label="Nome do Livro")
    edit_livro = ft.TextField(label="Editora do Livro")
    tipo_livro = ft.TextField(label="Tipo do Livro")
    ano_livro = ft.TextField(label="Ano de lançamento do Livro")
    autor_livro = ft.TextField(label="Autor do Livro")
    n_pag_livro = ft.TextField(label="Nº de Páginas do Livro")
    valor_livro = ft.TextField(label="Valor pago no Livro")
    lido_livro = ft.TextField(label="O livro foi lido?")
    popup_add_livro = ft.AlertDialog(
        open=False,
        modal=True,
        title=ft.Text("Qual seu livro novo?"),
        content=ft.Column(
            [
                ft.Row(
                    [
                        nome_livro,
                        edit_livro,
                    ]
                ),
                ft.Row(
                    [
                        tipo_livro,
                        ano_livro,
                    ]
                ),
                ft.Row(
                    [
                        autor_livro,
                        n_pag_livro,
                    ]
                ),
                ft.Row(
                    [
                        valor_livro,
                        lido_livro,
                    ]
                ),
            ],
            width=615,
        ),
        actions=[
            ft.ElevatedButton("Adicionar", on_click=add_livro, on_animation_end=ler_tabela),
        ],
    )

    app.add(ft.Row([botao_add_livro, botao_atualizar_dados]))


ft.app(target=main, view=ft.WEB_BROWSER)

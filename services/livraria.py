# Função principal (top-down)
def sistema_livraria(livros, busca=None, filtro=None):
    
    resultado = livros

    if busca:
        resultado = buscar_livros(resultado, busca)

    if filtro:
        resultado = filtrar_livros(resultado, filtro)

    return resultado


# Funcionalidades (User Stories)
def buscar_livros(livros, nome):
    return [l for l in livros if nome.lower() in l["titulo"].lower()]


def filtrar_livros(livros, criterio):
    return [l for l in livros if criterio(l)]


def ver_detalhes(livro):
    return livro

def adicionar_ao_carrinho(carrinho, livro):
    carrinho.append(livro)
    return carrinho

def realizar_pagamento(carrinho):
    if len(carrinho) == 0:
        return "Carrinho vazio"
    
    return "Pagamento realizado com sucesso"
from flask import request, jsonify
from src.model.produto_modal import (
    criar_produto, listar_produtos, buscar_produto, atualizar_produto, deletar_produto
)

def cadastrar_produto():
    data = request.get_json()
    nomeProduto = data.get('nomeProduto')
    preco = data.get('preco')
    quantidade = data.get('quantidade')

    message, status_code = criar_produto(nomeProduto, preco, quantidade)
    return jsonify(message), status_code

def listar_produtos_controller():
    produtos_list, status_code = listar_produtos()
    return jsonify(produtos_list), status_code

def buscar_produto_controller(id):
    produto, status_code = buscar_produto(id)
    return jsonify(produto), status_code

def atualizar_produto_controller(id):
    data = request.get_json()
    nomeProduto = data.get('nomeProduto')
    preco = data.get('preco')
    quantidade = data.get('quantidade')

    message, status_code = atualizar_produto(id, nomeProduto, preco, quantidade)
    return jsonify(message), status_code

def deletar_produto_controller(id):
    message, status_code = deletar_produto(id)
    return jsonify(message), status_code
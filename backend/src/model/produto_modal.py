# arquivo: app/models/produto_model.py

import mysql.connector
from src.database.conexao import criar_conexao

def criar_produto(nomeProduto, preco, quantidade):
    try:
        conexao = criar_conexao()
        cursor = conexao.cursor()
        cursor.execute("""
            INSERT INTO produtos (nomeProduto, preco, quantidade)
            VALUES (%s, %s, %s)
        """, (nomeProduto, preco, quantidade))
        conexao.commit()
        return {"message": "Produto cadastrado com sucesso"}, 201
    except Exception as erro:
        conexao.rollback()
        return {"error": str(erro)}, 500
    finally:
        cursor.close()
        conexao.close()

def listar_produtos():
    try:
        conexao = criar_conexao()
        cursor = conexao.cursor()
        cursor.execute("SELECT * FROM produtos")
        produtos = cursor.fetchall()
        produtos_list = [{"id": p[0], "nomeProduto": p[1], "preco": p[2], "quantidade": p[3]} for p in produtos]
        return produtos_list, 200
    except Exception as erro:
        return {"error": str(erro)}, 500
    finally:
        cursor.close()
        conexao.close()

def buscar_produto(id):
    try:
        conexao = criar_conexao()
        cursor = conexao.cursor()
        cursor.execute("SELECT * FROM produtos WHERE id = %s", (id,))
        produto = cursor.fetchone()
        if produto:
            produto_dict = {"id": produto[0], "nomeProduto": produto[1], "preco": produto[2], "quantidade": produto[3]}
            return produto_dict, 200
        else:
            return {"error": "Produto não encontrado"}, 404
    except Exception as erro:
        return {"error": str(erro)}, 500
    finally:
        cursor.close()
        conexao.close()

def atualizar_produto(id, nomeProduto, preco, quantidade):
    try:
        conexao = criar_conexao()
        cursor = conexao.cursor()
        cursor.execute("""
            UPDATE produtos
            SET nomeProduto = %s, preco = %s, quantidade = %s
            WHERE id = %s
        """, (nomeProduto, preco, quantidade, id))
        conexao.commit()
        if cursor.rowcount > 0:
            return {"message": "Produto atualizado com sucesso"}, 200
        else:
            return {"error": "Produto não encontrado"}, 404
    except Exception as erro:
        conexao.rollback()
        return {"error": str(erro)}, 500
    finally:
        cursor.close()
        conexao.close()

def deletar_produto(id):
    try:
        conexao = criar_conexao()
        cursor = conexao.cursor()
        cursor.execute("DELETE FROM produtos WHERE id = %s", (id,))
        conexao.commit()
        if cursor.rowcount > 0:
            return {"message": "Produto deletado com sucesso"}, 200
        else:
            return {"error": "Produto nao encontrado"}, 404
    except Exception as erro:
        conexao.rollback()
        return {"error": str(erro)}, 500
    finally:
        cursor.close()
        conexao.close()

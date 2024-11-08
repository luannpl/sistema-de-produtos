from flask import Flask
from flask_cors import CORS
from src.controller.produto_controller import (
    cadastrar_produto, listar_produtos_controller,
    buscar_produto_controller, atualizar_produto_controller, deletar_produto_controller
)


app = Flask(__name__)

CORS(app)

@app.route('/produtos', methods=['POST'])
def cadastrar_produto_route():
    return cadastrar_produto()

@app.route('/produtos', methods=['GET'])
def listar_produtos_route():
    return listar_produtos_controller()

@app.route('/produtos/<int:id>', methods=['GET'])
def buscar_produto_route(id):
    return buscar_produto_controller(id)

@app.route('/produtos/<int:id>', methods=['PUT'])
def atualizar_produto_route(id):
    return atualizar_produto_controller(id)

@app.route('/produtos/<int:id>', methods=['DELETE'])
def deletar_produto_route(id):
    return deletar_produto_controller(id)

if __name__ == '__main__':
    app.run(debug=True)
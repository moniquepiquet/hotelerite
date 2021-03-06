from flask import Blueprint
from flask import jsonify, request, Response
from src.business.cadastro import Cadastro
from src.entities.funcionario import Funcionario

funcionarios = Blueprint('funcionarios', __name__)

cadastro_funcionario = Cadastro()


@funcionarios.route("/cadastro", methods=['POST'])
def cadastrar_funcionario():
    dados = request.json

    funcionario = Funcionario(
        dados['nome'],
        dados['cpf'],
        dados['data_admissao'],
        dados['cargo'],
        dados['comissao'])

    cadastro_funcionario.cadastrar_funcionario(funcionario)

    return Response("Funcionario cadastrado!", 201)
    
@funcionarios.route("/consulta", methods=['GET'])
def consulta():
    cadastro = Cadastro()
    return (cadastro.consultar_por_matricula())
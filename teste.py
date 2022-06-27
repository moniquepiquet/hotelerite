from datetime import date
from src.business.cadastro import Cadastro
from src.entities.funcionario import Funcionario

today = date.today()

gran_finale = date(2022, 7, 18)

diff = gran_finale - today

print(diff.days)

# f1 = Funcionario(123, "Monique")

# cadastro = Cadastro()

# cadastro.cadastrar_funcionario(f1)

# f = cadastro.consultar_por_matricula(123)

# print(f.nome)
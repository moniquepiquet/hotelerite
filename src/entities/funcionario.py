from src.business.matricula import gera_matricula


class Funcionario:
    def __init__(self, nome, cpf, data_admissao, cargo, comissao) -> None:
        self.matricula: str = gera_matricula()
        self.nome: str = nome
        self.cpf: str = cpf
        self.data_admissao: str = data_admissao
        self.cargo: str = cargo
        self.comissao: str = comissao

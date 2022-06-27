from src.entities.funcionario import Funcionario


class Cadastro:
    def __init__(self) -> None:
        self.__funcionarios: list = []

    def cadastrar_funcionario(self, funcionario: Funcionario):
        self.__funcionarios.append(funcionario)

    def remover_por_matricula(self, matricula: int):
        funcionario = self.consultar_por_matricula(matricula)
        resposta = input(f"Deseja mesmo excluir o funcionário {funcionario.matricula}? [S/N]")

        if resposta == 'S' or resposta == 's':
            self.__funcionarios.remove(funcionario)
            return ("Funcionário removido")
        else:
            print("Operação cancelada")

    def consultar_por_matricula(self, matricula: int):
        funcionario = list(filter(lambda x: x.matricula ==
                           matricula, self.__funcionarios))

        if funcionario == []:
            raise IndexError("Funcionário não encontrado")  # criar a exception

        return funcionario[0]

    def alterar_dados(self):
        pass

    def listar_funcionarios(self):
        map(lambda x: print(x.nome), self.__funcionarios)

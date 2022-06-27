from numpy import random


def gera_matricula() -> str:
    amostra = list(map(str, random.randint(0, 10, 6)))
    matricula = ""

    for i in amostra:
        matricula += i

    return matricula

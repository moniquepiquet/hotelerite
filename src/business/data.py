from datetime import date


def dias_trabalhados(data_1, data_2):
    data_1 = date(2022, 7, 18)
    data_2 = date.today()

    diff = data_2 - data_1

    return diff.days

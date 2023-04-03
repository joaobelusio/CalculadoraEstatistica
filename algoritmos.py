from math import sqrt


def SomarValores():
    Alfabeto = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U",
                "V", "W", "X", "Y", "Z"]

    Acumulador = 0

    VariavelTemporaria = 0

    DesejaContinuar = "S"

    Valores = list()

    QuantidadeElementos = list()

    PopulacaoOuAmostra = 0

    while DesejaContinuar == "S":
        QuantidadeElementos.append(int(input(f"Digite quantos elementos o grupo '{Alfabeto[Acumulador]} possui: ")))
        VariavelTemporaria = float(input(f"Qual a o valor do grupo '{Alfabeto[Acumulador]}' ? "))
        for c in range(QuantidadeElementos[Acumulador]):
            Valores.append(VariavelTemporaria)
        Acumulador = Acumulador + 1
        DesejaContinuar = str(input("Deseja continuar [S/N] ? ").capitalize())
    PopulacaoOuAmostra = int(input("Deseja calcular População [0] ou Amostra [1] ? [0/1] "))
    SomatorioValores = 0

    for c in Valores:
        SomatorioValores = c + SomatorioValores
    return SomatorioValores





def CalcularMedia():
    Alfabeto = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U",
                "V", "W", "X", "Y", "Z"]

    Acumulador = 0

    VariavelTemporaria = 0

    DesejaContinuar = "S"

    Valores = list()

    QuantidadeElementos = list()

    PopulacaoOuAmostra = 0

    while DesejaContinuar == "S":
        QuantidadeElementos.append(int(input(f"Digite quantos elementos o grupo '{Alfabeto[Acumulador]} possui: ")))
        VariavelTemporaria = float(input(f"Qual a o valor do grupo '{Alfabeto[Acumulador]}' ? "))
        for c in range(QuantidadeElementos[Acumulador]):
            Valores.append(VariavelTemporaria)
        Acumulador = Acumulador + 1
        DesejaContinuar = str(input("Deseja continuar [S/N] ? ").capitalize())
    PopulacaoOuAmostra = int(input("Deseja calcular População [0] ou Amostra [1] ? [0/1] "))

    SomatorioQuantidadeElementos = 0
    SomatorioValores = 0
    for c in Valores:
        SomatorioValores = c + SomatorioValores
    for x in QuantidadeElementos:
        SomatorioQuantidadeElementos = x + SomatorioQuantidadeElementos
    return SomatorioValores/SomatorioQuantidadeElementos





def CalcularVariancia():
    Alfabeto = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U",
                "V", "W", "X", "Y", "Z"]

    Acumulador = 0

    VariavelTemporaria = 0

    DesejaContinuar = "S"

    Valores = list()

    QuantidadeElementos = list()

    PopulacaoOuAmostra = 0

    while DesejaContinuar == "S":
        QuantidadeElementos.append(int(input(f"Digite quantos elementos o grupo '{Alfabeto[Acumulador]} possui: ")))
        VariavelTemporaria = float(input(f"Qual a o valor do grupo '{Alfabeto[Acumulador]}' ? "))
        for c in range(QuantidadeElementos[Acumulador]):
            Valores.append(VariavelTemporaria)
        Acumulador = Acumulador + 1
        DesejaContinuar = str(input("Deseja continuar [S/N] ? ").capitalize())
    PopulacaoOuAmostra = int(input("Deseja calcular População [0] ou Amostra [1] ? [0/1] "))

    ListaSigma = list()
    Calculo = 0
    for c in Valores:
        Calculo = ((c-CalcularMedia())**2)
        ListaSigma.append(Calculo)
    if PopulacaoOuAmostra == 0:
        return sum(ListaSigma)/len(Valores)
    elif PopulacaoOuAmostra == 1:
        return sum(ListaSigma)/(len(Valores)-1)





def CalcularDesvioPadrao():
    Alfabeto = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U",
                "V", "W", "X", "Y", "Z"]

    Acumulador = 0

    VariavelTemporaria = 0

    DesejaContinuar = "S"

    Valores = list()

    QuantidadeElementos = list()

    PopulacaoOuAmostra = 0

    while DesejaContinuar == "S":
        QuantidadeElementos.append(int(input(f"Digite quantos elementos o grupo '{Alfabeto[Acumulador]} possui: ")))
        VariavelTemporaria = float(input(f"Qual a o valor do grupo '{Alfabeto[Acumulador]}' ? "))
        for c in range(QuantidadeElementos[Acumulador]):
            Valores.append(VariavelTemporaria)
        Acumulador = Acumulador + 1
        DesejaContinuar = str(input("Deseja continuar [S/N] ? ").capitalize())
    PopulacaoOuAmostra = int(input("Deseja calcular População [0] ou Amostra [1] ? [0/1] "))

    return sqrt(CalcularVariancia())


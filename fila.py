class Fila:
    def __init__(self):
        self.__dados = []

    def getFila(self):
        return self.__dados

    def inserirDado(self, novoDado):
        self.__dados.append(novoDado)

    def removerDado(self):
        self.__dados.pop(0)

    def remove(self, valor):
        pos = self.__dados.index(valor)
        carrosFora = []
        for i in range(0, pos+1):
            carrosFora.append(self.__dados[0])
            self.__dados.pop(0)

        for i in range(len(carrosFora) - 1):
            self.__dados.append(carrosFora[i])

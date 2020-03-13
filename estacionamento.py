from fila import Fila

def main():
    vagas = Fila()

    print('Comandos\n',
          'A - adicionar carro\n',
          'R - remover carro\n',
          'S - mostrar statatus do estacionamento\n',
          'E - Encerrar o programa')

    print()

    comando = input('Insira o comando desejado: ').upper()

    while comando != 'E':

        if comando == 'A':
            placa = input('Informe o numero da placa: ')
            vagas.inserirDado(placa)
            comando = input('Insira o comando desejado: ').upper()

        elif comando == 'R':
            placa = input('Informe a placa do carro que quer remover: ')
            vagas.remove(placa)

            comando = input('Insira o comando desejado: ').upper()

        elif comando == 'S':
            print(vagas.getFila())
            comando = input('Insira o comando desejado: ').upper()

main()

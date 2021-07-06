# faco a importacao da classe calculadora criada no arquivod calculadora.py
from calculadora import Calculadora

def main():
    # Crio/estancia uma objeto calculadora baseada na sua calsse
    # variavel = criacao de objeto a partir de uma classe
    calculadora = Calculadora()

    # Mostro na tela o resultado de uma subtracao
    print(calculadora.subtrai(calculadora.soma(1,3), 83))

    # Mostro na tela o resultado de uma subtracao
    print(calculadora.soma(123,123))


if __name__ == "__main__":
    main()
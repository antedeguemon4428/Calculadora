# Criando a CLASSE calculadaro
class Calculadora:
    
    # Metetodos da classe calculadora

    # Metodo de soma utilizado pela calculadora
    def soma(self, * numeros):
        resultado = 0
        for numero in numeros:
            resultado += numero

        return resultado
        
    # Metodo de subtracao utilizado pela calculadora
    def subtrai(self, *numeros):
        resultado = 0
        for numero in numeros:
            resultado -= numero

        return resultado

    def multiplica(self, *numeros):
        resultado = 0
        for numero in numeros:
            resultado *= numero

        return resultado

    def divide(self, *numeros):
        resultado = 0
        for numero in numeros:
            resultado /= numero

        return resultado
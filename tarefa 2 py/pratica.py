saida = ''
def adicao(a, b):
    return a + b

def subtracao(a, b):
    return a - b

def multiplicacao(x, y):
    x * y

def divisao(x, y):
        if y == 0:
            print ("Não foi possível realizar a subtração")
        return x / y
    
#Toda essa parte de cima são funções que vamos utilizar na calculadora de baixo.
#Vale lembrar que cada função tem sua operacao especifica

def calculadora(num1, num2, op):
    if op in ['+', 'adicao', 'adição']:
        resultado = adicao(num1, num2)
    elif op in ['-', 'subtracao', 'subtração']:
        resultado = subtracao(num1, num2)
    elif op in ['*', 'multiplicacao', 'multiplicação']:
        resultado = multiplicacao(num1, num2)
    elif op in ['/', 'divisão', 'divisao']:
        resultado = divisao(num1, num2)
    else:
        resultado = "Operação inválida"
    return resultado
#Cria-se uma função chamada calculadora, informando dois números e a operação
#Na linha 2 dessa função, utiliza-se a condição "IF" para habilitar diversos tipos de caracteres para escolher a operacao
#Na linha 3 dessa função, resgata a função anterior "Adição"
#Lembrar de sempre está colocando a aspas simples nos termos dentro dos colchetes
#A última condição deverá ser sempre a "ELSE"

while saida.lower() != 'n':
    num1 = float(input('Digite o primeiro número: '))
    num2 = float (input('Digite o segundo número: '))
    operacao = input('Digite a operação matemática desejada (+, -, *, / ou os nomes adicao, subtracao, multiplicacao, divisao)')
    resultado = calculadora (num1, num2, operacao)
    print ('Resultado da operação: ', resultado)
    saida = input('Deseja continuar? Digite S para SIM e N para NÃO')
print('Por favor, insira um número válido. ')
print('Programa encerrado')
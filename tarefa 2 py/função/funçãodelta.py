import math

def calculaDelta(coef1, coef2, coef3):
    delta = coef2*coef2 -4*coef1*coef3
    return delta

d = 0

a = eval(input('Entre com o coeficiente A: '))
b = eval(input('Entre com o coeficiente B: '))
c = eval(input('Entre com o coeficiente C: '))

d = calculaDelta(a, b, c)
print('O valor calculado do delta foi {d}')

if d>0:
    print('A equação 2 raízes reais.')
    raiz1=(-b + math.sqrt(d)/2*a)
    raiz2=(-b - math.sqrt(d)/2*a)
    print('O valor das raízes são: ', raiz1, 'e', raiz2)
elif d==0:
    print('A equação não tem raiz real.')
else:
    print('A equação tem 1 raiz real.')
    raiz=(-b + math.sqrt(d)/2*a)
    print('O valor da sua raiz é: ', raiz)


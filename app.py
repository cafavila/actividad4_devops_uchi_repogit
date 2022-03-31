import sys
def sumar(a, b):
    result = a + b
    return 'La suma es : {}'.format(result)

def restar(a, b):
    result = a -b
    return 'La resta es : '.format(result)    

def multiplicar(a, b):
    result = a * b
    return 'La multiplicacion es : '.format(result)

def dividir(a, b):
    result = a / b
    return 'La division es : '.format(result)

print ('Escoja la operacion que desea realizar')
print ('1.- Suma')
print ('2.- Resta')
print ('3.- Multiplicacion')
print ('4.- Division')
print ('5.- Todas')
op = input()
print ('Primer operando')
x = input()
print ('Segundo operando')
y = input()
if op>5:
    print ('Opcion No valida')
if op == 1 or op == 5:
    print (sumar(x, y))
if op == 2 or op == 5:
    print (restar(x, y))
if op == 3 or op == 5:
    print (multiplicar(x, y))
if op == 4 or op == 5:
    print (dividir(x, y))

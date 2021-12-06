from program import Calculadora

first = int(input('Ingrese un valor '))
second = int(input('Ingrese un segundo valor '))
resultado = Calculadora(first, second)

option= input("""Qué operación desea hacer?
aprete uno si los quiere sumar o dos si los quiere restar""")

if option=='1':
    print(resultado.suma())
elif option=='2':
    print(resultado.resta())
else:
    while option != '1' and option != '2':
        option = input('Por favor, escriba un valor válido ')
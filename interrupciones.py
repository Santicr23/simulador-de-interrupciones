
import random
import msvcrt

def suma(a, b):
    return a + b

def resta(a, b):
    return a - b

def multiplicacion(a, b):
    return a * b

def division(a, b):
    if b != 0:
        return a / b
    else:
        return "Error: división por cero"

operaciones = [suma, resta, multiplicacion, division]
prioridades = [1, 1, 2, 2] 

def obtener_operacion():
    return random.choice(operaciones)

while True:
    num1 = random.randint(1, 100)
    num2 = random.randint(1, 100)
    operacion_actual = obtener_operacion()
    print(f'Operación: {operacion_actual.__name__}')
    print(f'Números: {num1}, {num2}')
    resultado = operacion_actual(num1, num2)
    print(f'Resultado: {resultado}')
    print('Presiona "t" para cambiar de operación o cualquier otra tecla para continuar...')
    
    while True:
        if msvcrt.kbhit():
            tecla = msvcrt.getch().decode('utf-8').lower()
            if tecla == 't':
                operacion_actual_indice = operaciones.index(operacion_actual)
                
                for i in range(operacion_actual_indice + 1, len(operaciones)):
                    if prioridades[i] > prioridades[operacion_actual_indice]:
                        operacion_actual = operaciones[i]
                        break
                break  

    print('\n---\n')

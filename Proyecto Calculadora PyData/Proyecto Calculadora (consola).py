sw = True

print("Calculadora por consola")


def suma():
    num1 = int(input("Ingrese un numero: "))
    num2 = int(input("Ingrese otro numero: "))
    suma = num1 + num2
    print(f"La suma es {suma}")


def resta():
    num1 = int(input("Ingrese un numero: "))
    num2 = int(input("Ingrese otro numero: "))
    resta = num1 - num2
    print(f"La resta es {resta}")


def multiplicacion():
    num1 = int(input("Ingrese un numero: "))
    num2 = int(input("Ingrese otro numero: "))
    multiplicar = num1 * num2
    print(f"El producto es {multiplicar}")


def division():
    num1 = int(input("Ingrese un numero: "))
    num2 = int(input("Ingrese otro numero: "))
    division = num1 // num2
    print(f"El cociente es {division}")


while sw:
    menu = '''
    === Menu ===
    1. Suma
    2. Resta
    3. Multiplicacion
    4. Division
    5. Salir
    '''
    print(menu)
    option = int(input("Ingrese una opción: "))
    if option == 1:
        suma()
    elif option == 2:
        resta()
    elif option == 3:
        multiplicacion()
    elif option == 4:
        division()
    elif option == 5:
        print("Finalizado")
        sw = False
    else:
        print("Opción no válida")
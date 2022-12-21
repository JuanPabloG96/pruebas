import os

def sum(num1, num2):
    return num1 + num2

def rest(num1, num2):
    return num1 - num2

def div(num1, num2):
    return num1 / num2

def multi(num1, num2):
    return num1 * num2

salir = 0

while(salir == 0):
    print('\n1.- suma')
    print('2.- resta')
    print('3.- multiplicación')
    print('4.- division')
    print('5.- salir\n')

    selection = int(input('Seleccione una opción: '))
    
    if(selection != 5):
        if(selection >=1 and selection <= 5):
            num1 = float(input("\nIngrese el primer numero: "))
            num2 = float(input("Ingrese el segundo numero: "))

            if(selection == 1):
                print('\nEl resultado de la suma es: ' + str(sum(num1, num2)))
            elif(selection == 2):
                print('\nEl resultado de la resta es: ' + str(rest(num1, num2)))
            elif(selection == 3):
                print('\nEl resultado de la multiplicación es: ' + str(multi(num1, num2)))
            elif(selection == 4):
                print('\nEl resultado de la division es: ' + str(div(num1, num2)))
        else:
            print("\nOpción incorrecta")
    else:
        salir = 1
    os.system('pause')
    os.system('cls')
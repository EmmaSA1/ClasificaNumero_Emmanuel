def es_par_impar(numero):
    if numero % 2 == 0:
        print("El número es **par**.")
    else:
        print("El número es **impar**.")

def tipo_de_numero(numero):
    if numero > 0:
        print("El número es **positivo**.")
    elif numero < 0:
        print("El número es **negativo**.")
    else:
        print("El número es **cero**.")

def es_multiplo_de_5(numero):
    if numero % 5 == 0:
        print("El número **es múltiplo de 5**.")
    else:
        print("El número **no es múltiplo de 5**.")

def divisible_entre_3_y_4(numero):
    if numero % 3 == 0 and numero % 4 == 0:
        print("El número **es divisible entre 3 y 4 al mismo tiempo**.")
    else:
        print("El número **no es divisible entre 3 y 4 al mismo tiempo**.")

def menu():
    while True:
        print(" Menú ")
        print("1. Verificar si es par o impar")
        print("2. Verificar si es positivo, negativo o cero")
        print("3. Verificar si es múltiplo de 5")
        print("4. Verificar si es divisible entre 3 y 4 al mismo tiempo")
        print("5. Salir")
        
        opcion = input("Elige una opción (1-5): ")

        if opcion in ["1", "2", "3", "4"]:
            try:
                numero = int(input("Ingresa un número entero: "))
            except ValueError:
                print("Entrada inválida. Por favor, ingresa un número entero.")
                continue

            if opcion == "1":
                es_par_impar(numero)
            elif opcion == "2":
                tipo_de_numero(numero)
            elif opcion == "3":
                es_multiplo_de_5(numero)
            elif opcion == "4":
                divisible_entre_3_y_4(numero)
        elif opcion == "5":
            print("Saliendo del programa. ¡Hasta luego!")
            break
        else:
            print("Opción inválida. Por favor, elige una opción del 1 al 5.")

# Ejecutar el menú
menu()

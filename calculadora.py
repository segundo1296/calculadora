def suma(a, b):
    return a + b

def resta(a, b):
    return a - b

def multiplicacion(a, b):
    return a * b

def division(a, b):
    if b == 0:
        return "Error: No se puede dividir entre cero."
    return a / b

def calculadora():
    print("Bienvenido a la calculadora en Python")
    print("Selecciona la operación que deseas realizar:")
    print("1. Suma")
    print("2. Resta")
    print("3. Multiplicación")
    print("4. División")

    while True:
        try:
            opcion = input("Ingresa el número de la operación (1/2/3/4): ")

            if opcion in ['1', '2', '3', '4']:
                num1 = float(input("Ingresa el primer número: "))
                num2 = float(input("Ingresa el segundo número: "))

                if opcion == '1':
                    print(f"Resultado: {num1} + {num2} = {suma(num1, num2)}")
                elif opcion == '2':
                    print(f"Resultado: {num1} - {num2} = {resta(num1, num2)}")
                elif opcion == '3':
                    print(f"Resultado: {num1} * {num2} = {multiplicacion(num1, num2)}")
                elif opcion == '4':
                    print(f"Resultado: {num1} / {num2} = {division(num1, num2)}")
            else:
                print("Opción no válida. Intenta de nuevo.")
            
            continuar = input("¿Deseas realizar otra operación? (s/n): ")
            if continuar.lower() != 's':
                print("Gracias por usar la calculadora. ¡Hasta luego!")
                break
        except ValueError:
            print("Error: Ingresa solo números válidos.")

numeros = int(input("Ingresa la cantidad: "))
count = 0
suma_pares = 0

while count < numeros:
    num = int(input("Ingresar numero: "))
    if num % 2 == 0:
        suma_pares += num
    count += 1

if count > 0:
    promedio = suma_pares / count
    print(f"Promedio de numeros pares: {promedio}")
else:
    print("No se ingresaron numeros pares")

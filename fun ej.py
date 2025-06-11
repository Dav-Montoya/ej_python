#1
def sumar(a, b):
    print(a + b)

sumar(3, 5)

#2
def saludar(nombre):
    print(f"Hola, {nombre}")

saludar("david")

#3
def distinct(num):
    print(num % 2)
    return num % 2

numero = int(input("ingrese numero: "))
if distinct(numero) == 0:
    print("es par")
else:
    print("es impar")


a = int(input("numero a: "))
b = 2
resultado1 = a // b
resultado2 = resultado1 * b
resultado3 = a - resultado2
print("el valor entre a (%) b =", resultado3, ", esto es igual a funcion distinct")
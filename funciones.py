def saludar():
    print("Hola, bienvenido!")

saludar()

def saludar(nombre):
    print(f"Hola, {nombre}")

saludar("david")

def sumar(a, b):
    print(a + b)

sumar(3, 5)

def saludar(nombre="invitado"):
    print(f"Hola, {nombre}!")

saludar()
saludar("lucia")
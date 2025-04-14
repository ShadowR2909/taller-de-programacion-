import random
import math

# Ejercicio 1: Máximo entre tres números
def maximo_tres_numeros(a, b, c):
    return max(a, b, c)

# Ejercicio 2: Máximo entre diez números
def maximo_diez_numeros(numeros):
    return max(numeros)

# Ejercicio 3: Operaciones con vectores
def cargar_vector(tamano):
    return [random.randint(0, 9) for _ in range(tamano)]

def suma_vector(vector):
    return sum(vector)

def suma_vectores(v1, v2):
    return [v1[i] + v2[i] for i in range(len(v1))]

# Ejercicio 4: Contar vocales y consonantes
def contar_vocales(palabra):
    vocales = "aeiouAEIOU"
    return sum(1 for letra in palabra if letra in vocales)

def contar_consonantes(palabra):
    consonantes = "bcdfghjklmnpqrstvwxyzBCDFGHJKLMNPQRSTVWXYZ"
    return sum(1 for letra in palabra if letra in consonantes)

# Ejercicio 5: Menú de operaciones con números
def calcular_potencia(x, k):
    return x ** k

def cantidad_digitos(x):
    return len(str(x))

def es_capicua(x):
    x_str = str(x)
    return x_str == x_str[::-1]

# Ejercicio 6: Operaciones con matrices
def cargar_matriz(m, n):
    return [[random.randint(0, 9) for _ in range(n)] for _ in range(m)]

def sumar_matrices(matriz_a, matriz_b):
    m = len(matriz_a)
    n = len(matriz_a[0])
    matriz_c = [[matriz_a[i][j] + matriz_b[i][j] for j in range(n)] for i in range(m)]
    return matriz_c

def multiplicar_matrices(matriz_a, matriz_b):
    m = len(matriz_a)
    n = len(matriz_a[0])
    matriz_c = [[matriz_a[i][j] * matriz_b[i][j] for j in range(n)] for i in range(m)]
    return matriz_c

def mostrar_matriz(matriz):
    for fila in matriz:
        print(fila)

# Ejercicio 7: Operaciones con matrices cuadradas
def suma_diagonal_principal(matriz):
    return sum(matriz[i][i] for i in range(len(matriz)))

def factorial(numero):
    if numero == 0 or numero == 1:
        return 1
    else:
        return numero * factorial(numero - 1)

def filtrar_mayor_o_igual_factorial(matriz, suma_diagonal):
    elementos = [matriz[i][j] for i in range(len(matriz)) for j in range(len(matriz))]
    vector_resultante = [elemento for elemento in elementos if factorial(elemento) >= suma_diagonal]
    return vector_resultante

def eliminar_repetidos(vector):
    return list(set(vector))

def ordenar_vector(vector):
    vector.sort()
    return vector

# Ejercicio 8: Gestión de electrodomésticos
def cargar_matriz_electrodomesticos():
    matriz = []
    cantidad = int(input("Ingrese la cantidad de electrodomésticos: "))
    
    for _ in range(cantidad):
        nombre = input("Nombre del electrodoméstico: ")
        proveedor = input("Proveedor: ")
        precio = input("Precio: ")
        while not precio.isdigit():
            precio = input("Precio inválido. Ingrese un número: ")
        cantidad_stock = input("Cantidad en stock: ")
        while not cantidad_stock.isdigit():
            cantidad_stock = input("Cantidad inválida. Ingrese un número: ")
        
        matriz.append([nombre, proveedor, int(precio), int(cantidad_stock)])
    
    return matriz

def mostrar_por_proveedor(matriz, proveedor_buscado):
    print(f"Electrodomésticos del proveedor {proveedor_buscado}:")
    for electrodomestico in matriz:
        if electrodomestico[1] == proveedor_buscado:
            print(electrodomestico)

def mostrar_menor_precio(matriz):
    menor_precio = min(matriz, key=lambda x: x[2])
    print(f"Electrodoméstico con menor precio: {menor_precio}")

def mostrar_stock_positivo(matriz):
    print("Electrodomésticos con stock positivo:")
    for electrodomestico in matriz:
        if electrodomestico[3] > 0:
            print(electrodomestico)

# Ejercicio 19: Lista de pacientes
def ingresar_paciente(lista_espera, paciente, urgencia=False):
    if urgencia:
        lista_espera.insert(0, paciente)
    else:
        lista_espera.append(paciente)

def atender_paciente(lista_espera):
    if lista_espera:
        paciente_atendido = lista_espera.pop(0)
        print(f"Paciente atendido: {paciente_atendido}")
        return paciente_atendido
    else:
        print("No hay pacientes en la lista de espera.")
        return None

def pacientes_faltantes(lista_espera, paciente_x):
    if paciente_x in lista_espera:
        faltantes = lista_espera.index(paciente_x)
        print(f"Faltan {faltantes} pacientes para atender al paciente {paciente_x}.")
        return faltantes
    else:
        print(f"El paciente {paciente_x} no está en la lista de espera.")
        return -1

# Ejercicio 10: Máquina tragamonedas
def generar_vector_simbolos():
    simbolos = ["O", "X", "7"]
    return [random.choice(simbolos) for _ in range(9)]

def rotar_vector(vector, posiciones):
    posiciones %= len(vector)
    return vector[-posiciones:] + vector[:-posiciones]

def jugar_tragamonedas():
    rodillo1 = generar_vector_simbolos()
    rodillo2 = generar_vector_simbolos()
    rodillo3 = generar_vector_simbolos()

    posiciones1 = random.randint(0, 9)
    posiciones2 = random.randint(0, 9)
    posiciones3 = random.randint(0, 9)

    rodillo1_rotado = rotar_vector(rodillo1, posiciones1)
    rodillo2_rotado = rotar_vector(rodillo2, posiciones2)
    rodillo3_rotado = rotar_vector(rodillo3, posiciones3)

    # Mostrar resultados
    print("Rodillos después de la rotación:")
    print(f"Rodillo 1: {rodillo1_rotado}")
    print(f"Rodillo 2: {rodillo2_rotado}")
    print(f"Rodillo 3: {rodillo3_rotado}")

    # Verificar premios
    if rodillo1_rotado[0] == rodillo2_rotado[0] == rodillo3_rotado[0]:
        simbolo_ganador = rodillo1_rotado[0]
        if simbolo_ganador == "X":
            print("¡Ganó 10 fichas!")
        elif simbolo_ganador == "O":
            print("¡Ganó 100 fichas!")
        elif simbolo_ganador == "7":
            print("¡Ganó 1000 fichas!")

def contar_digitos():
    num = input("Ingrese número entero: ")
    if num == "0":
        print("Dígitos: 1")
    else:
        print("Dígitos:", len(num.lstrip("-")))

def contar_decimal():
    num = input("Ingrese número decimal: ").replace(",", ".")
    partes = num.split(".")
    entero = partes[0].lstrip("+-")
    decimal = partes[1] if len(partes) > 1 else ""
    print(f"Dígitos enteros: {len(entero)}")
    print(f"Dígitos decimales: {len(decimal)}")

def compuestos():
    nums = list(map(int, input("Vector (sep. espacios): ").split()))
    compuestos = []
    for n in nums:
        divisores = 0
        for i in range(1, n+1):
            if n % i == 0:
                divisores += 1
        if divisores > 2:
            compuestos.append(n)
    print("Compuestos:", compuestos)

def invertir_vector():
    vec = input("Vector (sep. espacios): ").split()
    print("Con auxiliar:", vec[::-1])
    vec = list(vec)
    for i in range(len(vec)//2):
        vec[i], vec[-i-1] = vec[-i-1], vec[i]
    print("Sin auxiliar:", vec)

def filtrar_lista():
    lista = list(map(float, input("Lista A: ").split()))
    nueva = []
    for num in lista:
        entero = str(abs(int(num)))
        pares = 0
        impares = 0
        for d in entero:
            if int(d) % 2 == 0:
                pares += 1
            else:
                impares += 1
        if pares == 2 and impares >= 2:
            nueva.append(num)
    print("Lista B:", nueva)

def insertar_multiplos():
    K = int(input("Valor K: "))
    lista = list(map(int, input("Lista: ").split()))
    nueva = []
    for n in lista:
        nueva.append(n)
        if n % K == 0 and n != 0:
            nueva.append(K)
    print("Resultado:", nueva)

def promedios_matriz():
    M = int(input("Filas: "))
    N = int(input("Columnas: "))
    matriz = []
    for _ in range(M):
        fila = list(map(float, input().split()))
        matriz.append(fila)
    
    print("\nMatriz:")
    for fila in matriz:
        print(fila)
    
    print("\nPromedios filas:")
    for i in range(M):
        suma = sum(matriz[i])
        print(f"Fila {i+1}: {suma/N}")
    
    print("\nPromedios columnas:")
    for j in range(N):
        suma = 0
        for i in range(M):
            suma += matriz[i][j]
        print(f"Col {j+1}: {suma/M}")

def punto_silla():
    M = int(input("Filas: "))
    N = int(input("Columnas: "))
    matriz = []
    for _ in range(M):
        fila = list(map(int, input().split()))
        matriz.append(fila)
    
    k = int(input("Fila k: "))
    h = int(input("Columna h: "))
    
    max_fila = max(matriz[k])
    min_col = min(matriz[i][h] for i in range(M))
    print("Es punto silla" if matriz[k][h] == max_fila == min_col else "No es punto silla")

def matriz_simetrica():
    M = int(input("Tamaño: "))
    matriz = []
    for _ in range(M):
        fila = list(map(int, input().split()))
        matriz.append(fila)
    
    simetrica = True
    for i in range(M):
        for j in range(M):
            if matriz[i][j] != matriz[j][i]:
                simetrica = False
                break
        if not simetrica:
            break
    print("Simétrica" if simetrica else "No simétrica")

def main():
    while True:
        print("\nMenú Principal")
        print("1. Contar dígitos entero")
        print("2. Contar dígitos decimal")
        print("3. Números compuestos")
        print("4. Invertir vector")
        print("5. Filtrar lista")
        print("6. Insertar múltiplos")
        print("7. Promedios matriz")
        print("8. Punto silla")
        print("9. Matriz simétrica")
        print("0. Salir")
        
        opcion = input("Opción: ")
        
        if opcion == "0":
            print("¡Hasta luego!")
            break
            
        elif opcion == "1":
            contar_digitos()
        elif opcion == "2":
            contar_decimal()
        elif opcion == "3":
            compuestos()
        elif opcion == "4":
            invertir_vector()
        elif opcion == "5":
            filtrar_lista()
        elif opcion == "6":
            insertar_multiplos()
        elif opcion == "7":
            promedios_matriz()
        elif opcion == "8":
            punto_silla()
        elif opcion == "9":
            matriz_simetrica()
        else:
            print("Opción inválida")

if __name__ == "__main__":
    main()

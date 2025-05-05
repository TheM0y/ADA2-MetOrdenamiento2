def shell_sort(arr):
    print("\nProceso de ShellSort:")
    n = len(arr)
    gap = n // 2
    while gap > 0:
        print(f"Gap: {gap}")
        for i in range(gap, n):
            temp = arr[i]
            j = i
            while j >= gap and arr[j - gap] > temp:
                arr[j] = arr[j - gap]
                j -= gap
                print(f"Moviendo {arr[j]} a la posición {j + gap}: {arr}")
            arr[j] = temp
            print(f"Insertado {temp} en la posición {j}: {arr}")
        gap //= 2
    return arr

def quicksort(arr, depth=0):
    indent = "  " * depth
    if len(arr) <= 1:
        return arr
    pivot = arr[len(arr) // 2]
    print(f"{indent}Pivot: {pivot}")
    left = [x for x in arr if x < pivot]
    print(f"{indent}Izquierda: {left}")
    middle = [x for x in arr if x == pivot]
    print(f"{indent}Centro: {middle}")
    right = [x for x in arr if x > pivot]
    print(f"{indent}Derecha: {right}")
    return quicksort(left, depth + 1) + middle + quicksort(right, depth + 1)

def heapify(arr, n, i, depth=0):
    indent = "  " * depth
    largest = i
    l = 2 * i + 1
    r = 2 * i + 2
    if l < n and arr[l] > arr[largest]:
        largest = l
    if r < n and arr[r] > arr[largest]:
        largest = r
    if largest != i:
        print(f"{indent}Intercambiando {arr[i]} con {arr[largest]}")
        arr[i], arr[largest] = arr[largest], arr[i]
        print(f"{indent}Estado actual: {arr}")
        heapify(arr, n, largest, depth + 1)

def heap_sort(arr):
    print("\nProceso de HeapSort:")
    n = len(arr)
    for i in range(n // 2 - 1, -1, -1):
        heapify(arr, n, i)
    print("Max Heap creado:", arr)
    for i in range(n - 1, 0, -1):
        print(f"Intercambiando {arr[0]} con {arr[i]}")
        arr[i], arr[0] = arr[0], arr[i]
        print(f"Estado actual: {arr}")
        heapify(arr, i, 0)
    return arr

def counting_sort_for_radix(arr, exp):
    n = len(arr)
    output = [0] * n
    count = [0] * 10
    print(f"Contando con exp={exp}")
    for i in range(n):
        index = (arr[i] // exp) % 10
        count[index] += 1
    print("Conteo:", count)
    for i in range(1, 10):
        count[i] += count[i - 1]
    i = n - 1
    while i >= 0:
        index = (arr[i] // exp) % 10
        output[count[index] - 1] = arr[i]
        count[index] -= 1
        i -= 1
    for i in range(n):
        arr[i] = output[i]
    print(f"Resultado parcial con exp={exp}: {arr}")

def radix_sort(arr):
    print("\nProceso de Radix Sort:")
    if not arr:
        return arr
    max1 = max(arr)
    exp = 1
    while max1 // exp > 0:
        counting_sort_for_radix(arr, exp)
        exp *= 10
    return arr

def main():
    print("Bienvenido al programa de ordenamiento")
    cantidad = int(input("Ingrese la cantidad de números: "))
    numeros = []
    for i in range(cantidad):
        num = int(input(f"Ingrese el número {i+1}: "))
        numeros.append(num)

    while True:
        print("\nMenú de métodos de ordenamiento:")
        print("1. ShellSort")
        print("2. Quicksort")
        print("3. Heapsort")
        print("4. Radix Sort")
        print("5. Salir")
        opcion = input("Seleccione una opción (1-5): ")

        if opcion == '1':
            resultado = shell_sort(numeros.copy())
            print("Resultado final:", resultado)
        elif opcion == '2':
            print("\nProceso de Quicksort:")
            resultado = quicksort(numeros.copy())
            print("Resultado final:", resultado)
        elif opcion == '3':
            resultado = heap_sort(numeros.copy())
            print("Resultado final:", resultado)
        elif opcion == '4':
            resultado = radix_sort(numeros.copy())
            print("Resultado final:", resultado)
        elif opcion == '5':
            print("Saliendo del programa...")
            break
        else:
            print("Opción inválida, por favor elija del 1 al 5.")

if __name__ == "__main__":
    main()

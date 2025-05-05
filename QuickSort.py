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

def main():
    cantidad = int(input("Ingrese la cantidad de números: "))
    numeros = [int(input(f"Ingrese el número {i+1}: ")) for i in range(cantidad)]
    print("\nProceso de Quicksort:")
    resultado = quicksort(numeros.copy())
    print("Resultado final:", resultado)

if __name__ == "__main__":
    main()

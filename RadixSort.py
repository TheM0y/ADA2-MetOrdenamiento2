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
    cantidad = int(input("Ingrese la cantidad de números: "))
    numeros = [int(input(f"Ingrese el número {i+1}: ")) for i in range(cantidad)]
    resultado = radix_sort(numeros.copy())
    print("Resultado final:", resultado)

if __name__ == "__main__":
    main()

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

def main():
    cantidad = int(input("Ingrese la cantidad de números: "))
    numeros = [int(input(f"Ingrese el número {i+1}: ")) for i in range(cantidad)]
    resultado = shell_sort(numeros.copy())
    print("Resultado final:", resultado)

if __name__ == "__main__":
    main()

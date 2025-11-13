numeros = [2 * (i + 1) for i in range(25)]  # [2,4,6,...,50]
def busca_binaria_verbose(arr, alvo):
    low = 0
    high = len(arr) - 1
    passo = 1
    while low <= high:
        mid = (low + high) // 2
        print(f"Passo {passo}: low={low}, high={high}, mid={mid}, arr[mid]={arr[mid]}")
        if arr[mid] == alvo:
            print(f"-> Encontrado {alvo} na posição (índice) {mid}.")
            return mid
        elif arr[mid] < alvo:
            print(f"   {arr[mid]} < {alvo} -> mover 'low' para mid+1 ({mid+1})")
            low = mid + 1
        else:
            print(f"   {arr[mid]} > {alvo} -> mover 'high' para mid-1 ({mid-1})")
            high = mid - 1
        passo += 1
    print(f"-> {alvo} NÃO encontrado na lista.")
    return -1
try:
    alvo = int(input("Digite o número a procurar: "))
    busca_binaria_verbose(numeros, alvo)
except ValueError:
    print("Por favor digite um número inteiro válido.")

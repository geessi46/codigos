tabuleiro = [" "] * 9
jogador = "X"

def exibir():
    print(f"{tabuleiro[0]} | {tabuleiro[1]} | {tabuleiro[2]}")
    print("--+---+--")
    print(f"{tabuleiro[3]} | {tabuleiro[4]} | {tabuleiro[5]}")
    print("--+---+--")
    print(f"{tabuleiro[6]} | {tabuleiro[7]} | {tabuleiro[8]}")

def venceu(j):
    c = tabuleiro
    return ((c[0]==c[1]==c[2]==j) or (c[3]==c[4]==c[5]==j) or (c[6]==c[7]==c[8]==j) or
            (c[0]==c[3]==c[6]==j) or (c[1]==c[4]==c[7]==j) or (c[2]==c[5]==c[8]==j) or
            (c[0]==c[4]==c[8]==j) or (c[2]==c[4]==c[6]==j))

for rodada in range(9):
    exibir()
    pos = int(input(f"Jogador {jogador}, escolha (0-8): "))
    if tabuleiro[pos] != " ":
        print("Posição ocupada, tente outra.")
        continue
    tabuleiro[pos] = jogador
    if venceu(jogador):
        exibir()
        print(f"Jogador {jogador} venceu!")
        break
    jogador = "O" if jogador == "X" else "X"
else:
    exibir()
    print("Empate!")

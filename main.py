import random

# Uma função responsável por gerar 5 números aleatórios.
def numAleatorios():
    list_pc = []
    i = 1

    while i <= 5:
        numero = random.randint(1, 10)

        if numero not in list_pc:
            list_pc.append(numero)
            i += 1

    return list_pc


# Uma função responsável por verificar a quantidade de acertos do usuário.
def acertos(pc, user):
    pontos = 0

    for n in user:
        if n in pc:
            pontos += 1

    return pontos


list_user = []
x = 1

while x <= 5:
    num = int(input("Digite um número: "))

    if num not in list_user:
        list_user.append(num)
        x += 1


num_pc = numAleatorios()
print(f"Números Sorteados: {num_pc}")

pontuacao = acertos(num_pc, list_user)
print(f"Você fez {pontuacao} ponto(s)")
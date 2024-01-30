from palavras import palavra

letras_chute = []
chances = 4
ganhou = False

while True:

    print(letras_chute)

    for letra in palavra:
        if letra.lower() in letras_chute:
            print(letra, end=" ")
        else:
            print('_', end=" ")
    
    print(' ')
    print(' ')
    print(f'Você ainda tem {chances} tentativas')
    print(' ')

    letra_tentativa = input('Escolha uma letra: ')
    letras_chute.append(letra_tentativa.lower())

    if letra_tentativa.lower() not in palavra.lower():
        chances -= 1

    ganhou = True
        
    for letra in palavra:    
        if letra.lower() not in letras_chute:
            ganhou = False

    if chances == 0 or ganhou:
        break
    

if ganhou:
    # encerra o jogo
    print(f'Parabéns, você ganhou. A palavra é: {palavra}')
else:
    # encerra o jogo
    print(f'Você perdeu. A palavra era: {palavra}')

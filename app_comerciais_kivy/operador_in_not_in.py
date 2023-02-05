


cores = ['azul', 'amarelo', 'vermelho ', 'branca']

while True:
    cor = input("Digite o nome de uma cor ou estão, 0 para sair do programa : ")

    if(cor=='0'):
        break
    elif cor in cores:
        print("Essa cor está contida!")
    else:
        print("Essa cor não está contida")

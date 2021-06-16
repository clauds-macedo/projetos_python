from time import sleep

def pessoas():
    p = open('pessoas.txt', 'a')
    pessoa = str(input("Digite o nome de uma pessoa: ")).capitalize()
    while True:
        try:
            idade = int(input("Digite a idade dessa pessoa: "))
        except:
            print("Digite um número inteiro válido!!!!!!!!!!")
        else:
            break
    p.write(f'Nome: {pessoa:19} Idade: {idade} anos\n')
    p.close()


def mostrarPessoas():
    teste = open('pessoas.txt', 'r')
    for linha in teste:
        linha = linha.replace('\n', '')
        print(f'{linha}\n', end= '')



def linhas():
    print("\033[1;30m-="*20)


def menu():
    msg = 'Menu Principal'
    linhas()
    print("{}".format(msg).center(40))
    linhas()
    print("\033[1;93m 1-", end='')
    print(" \033[1;34mVer pessoas cadastradas")
    print("\033[1;93m 2-", end='')
    print(" \033[1;34mCadastrar nova pessoa")
    print("\033[1;93m 3-", end='')
    print(' \033[1;34mSair do programa')
    linhas()


#Programa principal

while True:
    menu()
    try:
        option = int(input("Sua opção: "))
    except:
        print("Erro! Digite um número inteiro.")
    else:
        if option == 1:
            linhas()
            print("{:^40}".format("Pessoas cadastradas"))
            linhas()
            mostrarPessoas()
            sleep(1.5)

        elif option == 2:
            pessoas()

        elif option == 3:
            break
        else:
            print("Valor inválido, tente novamente!!!!!!!")
print("Obrigado e volte sempre!!!!")



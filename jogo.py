
import random
import os            #sistema operacional
vit = 0
der = 0
emp = 0
while True:
    print('============================================')
    print("=================== JOGO =================== \n")
    nome = input('Digite seu nome (ou "sair" para encerrar): ')
    if nome == 'sair' or nome == 'SAIR':
        print('                                   ')
        print('=============== FIM DE JOGO ================\n')
        break #ENCERRA O JOGO

    rodadas = int(input(f"{nome}, agora digite a quantidade de rodadas: "))
    os.system('cls') #limpar a tela


    for i in range(rodadas):

        maq = random.randint(1, 3)

        for x in range(1000):
             print('============================================')
             print("=================== JOGO =================== \n")
             print("1 - PEDRA")
             print("2 - PAPEL")
             print("3 - TESOURA \n")
             jogada = int(input('FAÇA SUA JOGADA: '))
             print('                                   ')
             if jogada !=1 and jogada !=2 and jogada!=3:
                    print('ERRO! JOGADA INVÁLIDA')
                    cont = input('Pressione ENTER para tentar novamente...')
                    os.system('cls') #Limpar a tela
             else:
                 break

        if jogada ==1 or jogada ==2 or jogada ==3:

            #SE PESSOA ESCOLHER PEDRA
            if jogada ==1 and maq ==2:
                print('VOCE PERDEU! EU ESCOLHI PAPEL :) ')
                der+=1
            elif jogada ==1 and maq ==3:
                print('PARABÉNS VOCÊ VENCEU! INFELIZMENTE ESCOLHI TESOURA :(')
                vit+=1
            elif jogada ==1 and maq ==1:
                print('EMPATE! EU TAMBEM ESCOLHI PEDRA ;)')
                emp+=1

            #SE PESSOA ESCOLHER PAPEL
            elif jogada ==2 and maq ==1:
                print('PARABÉNS VOCÊ VENCEU! INFELIZMENTE ESCOLHI PEDRA :(')
                vit+=1
            elif jogada ==2 and maq ==3:
                print('VOCE PERDEU! EU ESCOLHI TESOURA :) ')
                der+=1
            elif jogada ==2 and maq ==2:
                print('EMPATE! EU TAMBEM ESCOLHI PAPEL ;) ')
                emp+=1

            #SE PESSOA ESCOLHER TESOURA
            elif jogada ==3 and maq ==1:
                print('VOCE PERDEU! EU ESCOLHI PEDRA :)')
                der+=1
            elif jogada ==3 and maq ==2:
                print('PARABÉNS VOCÊ VENCEU! INFELIZMENTE ESCOLHI PAPEL :( ')
                vit+=1
            elif jogada ==3 and maq ==3:
                print('EMPATE! EU TAMBEM ESCOLHI TESOURA ;)')
                emp+=1
            print('                                                            ')
            

            cont = input('Pressione ENTER para continuar...')
            os.system('cls') #limpar a tela
    print('============================================')
    print('========== RELATÓRIO DAS RODADAS ===========\n')
    print(f'VITÓRIAS: {vit}')
    print(f'DERROTAS: {der}')
    print(f'EMPATES: {emp}\n')

    print('================ FIM DE JOGO ===============\n')

    novojogo = input('Pressione ENTER para jogar novamente... ')
    os.system('cls') #Limpar a tela

    vit =0
    der = 0
    emp = 0





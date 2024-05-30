import time
from os import system
from funcoes import *
import keyboard                 #pip install keyboard
import sys


#Solicitar ao usuário a quantidades de CLPs, IP e portas
system('cls')
qtd_CLPs = int(input('Informe a quantidade de CLPs: '))

ip = input('Informe o IP: ')
porta_inicial = int(input('Informe a porta inicial: '))

CLPs_dados = [0]   #Lista para guardar os dicionários com informações dos CLPs ignorando a posição 0
#Criar dicionários com dados dos CLPs e guarda em CLP_dados
for i in range(1, qtd_CLPs+1):
    clp = {
        "nome": 'CLP'+str(i),
        "ip": ip,
        "porta": porta_inicial+i-1,
        "Temperatura": {"endereco": 0, "valor": 0},
        "Vazao": {"endereco": 1, "valor": 0},
        "Pressao": {"endereco": 2, "valor": 0},
        "status": False
    }
    CLPs_dados.append(clp)


#Criando conexões com os clientes
CLP = [0]
for i in range(1, qtd_CLPs+1):
    clp = CLPs_dados[i]
    CLP.append('')
    CLP[i] = conectar(ip, clp["porta"])
    if verificarConexao(CLP[i]):
        clp["status"] = True
    CLPs_dados[i] = clp
time.sleep(2)


while True:
    while True:
        
        #Imprimir na tela todos os CLPs e perguntar qual o usuário deseja verificar
        try:
            system('cls')
            imprimirClientes(CLPs_dados, qtd_CLPs)
            selector = int(input('Qual CLP você deseja verificar? \n[Ou pressione 0 para fechar o programa.]\n'))

            #Se pressionar zero, todas as conexões são encerradas e o programa fecha
            if selector == 0:
                for i in range(1, qtd_CLPs+1):
                    if verificarConexao(CLP[i]):
                        encerrarConexao(CLP[i])
                system('cls')
                sys.exit()
            elif selector>0 and selector<=qtd_CLPs and verificarConexao(CLP[selector]):
                break
            elif not(selector>0 and selector<=qtd_CLPs):
                system('cls')
                print("Por favor, digite um número inteiro do intervalo.")
                time.sleep(2)
            else: 
                system('cls')
                print('Não há conexão com este CLP.')
                time.sleep(2)
        except ValueError:
            system('cls')
            print("Por favor, digite um número inteiro válido.")
            time.sleep(2)

    #Imprimir dados do CLP solicitado
    while True:
        system('cls')
        imprimirCLP(CLPs_dados[selector], CLP[selector])
        print("Pressione a tecla 'Esc' para retornar.")
    
        start_time = time.time()
        while time.time() - start_time < 1:  
            if keyboard.is_pressed('esc'):
                system('cls')
                break
        if keyboard.is_pressed('esc'):
            break
        
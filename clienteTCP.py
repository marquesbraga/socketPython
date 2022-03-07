#Script para a criação de um cliente tcp

import socket
import sys


def main():
    #criando o socket
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM, 0) 
    except socket.error as e:
        print('Conexão falhou!!!')
        print(f'Erro: {e}')
        sys.exit()

    print('Socket criado com sucesso.')
    
    hostalvo = input('Digite o host a ser conectado: ')
    portalalvo = int(input('Digite a porta a ser conectado: '))

    
    try:
        s.connect((hostalvo,portalalvo))
        print('Cliente tcp cconcetado com sucesso.')
        s.shutdown(2) # fechar conexão
    except socket.error  as e:
        print('Conexão falhou')
        print(f'Erro: {e}')
        sys.exit()
        
        
if __name__ == "__main__":
    main()
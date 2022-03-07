#Script para a criação de cliente UDP

import socket

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

print('Cliente socket criando com sucesso!!!')

host = 'localhost'
porta = 5433
mensagem = 'Olá servidor, ola mundo'

try:
    print('Cliente tentando mandar msg')
    s.sendto(mensagem.encode(),(host,porta))
    
    dados, servidor = s.recvfrom(4096)
    dados = dados.decode()
    print('Cliente ' + dados)
finally:
    print('CLiente: Fechando a conexão')
    s.close()
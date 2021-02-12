# -*- coding: utf-8 -*-
import socket
usuarios = ["contato","comercial","financeiro","vendas","atendimento","sac","root", "trial"]
alvo = raw_input("ALVO: ")
for usuario in usuarios:
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM) #Criar Socket para conectar ao servidor SMTP
    sock.connect((alvo,25)) #Criar Socket para conectar ao servidor SMTP
    sock.recv(1024) #Recebe o banner do servidor
    sock.send("VRFY " + usuario + "\n") #Envia via send( do comando objeto SOCK o VRFY para verificar se o usuario existe)
    smtp_resultado = sock.recv(1024) #Recebe 1024 bytes de entrada, sendo cada divisao deles uma  resposta diferente para a solicitacao
    sock.close() #Finaliza o socket criado
    if "252" in smtp_resultado: #Faz a verificacao do resultado.
        print usuario + "-> Valido!"
    elif "550" in smtp_resultado:
        print usuario+ "-> Usuario Invalido!"
    elif "503" in smtp_resultado:
        print "Servidor requer autenticacao"
        break
    elif "500" in smtp_resultado:
        print "Comando VRFY nao supotado pelo servidor"
        break
    else:
        print "Resposta do servidor: ", smtp_resultado
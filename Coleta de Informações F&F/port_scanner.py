# -*- coding: utf-8 -*-
import socket
host = input("ALVO: ")
portas = [80,443,21,22]
for porta in range(1000):
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.settimeout(1)
    resultado = sock.connect_ex((host, porta))
    sock.close()
    if resultado == 0:
        print (porta)

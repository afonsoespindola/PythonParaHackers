# -*- coding: utf-8 -*-
from  scapy.all import *
#host = raw_input("ALVO: ")
pacote_ip_alvo = IP(dst = "191.243.8.88")
pacote_tcp = TCP(dport=portas, flags="S")
pacote = pacote_ip_alvo/pacote_tcp
ans, unans = sr(pacote, inter=0.1, timeout=1)
print "Porta\tEstado"
portas = [21,22,25,80,106,110,143,465,993,995]
for pacote_recebido in ans:
    print pacote_recebido[1][IP].sport, \
    "\t", pacote_recebido[1][TCP].sprintf("%flags%")

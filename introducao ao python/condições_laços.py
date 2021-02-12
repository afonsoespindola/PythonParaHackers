'''
for numero in range(4,5): #1,5
    print numero
'''
'''
lista = [1,2,3,4,5, "arroz", "lentilha", 8]

for numero in lista:
    print numero

texto = "Python para Hackers"
for letra in texto:
    print letra
'''


#WHILE

criterio_parada = 0
criterio_parada_dois = 0
while criterio_parada != 10:
    print criterio_parada
    if criterio_parada == 6:
        print "seis"
    if criterio_parada == 9:
        criterio_parada_dois = criterio_parada_dois+1
    if criterio_parada_dois == 3:
        print "FIM DO PROGRAMA"
        break
    if criterio_parada == 9:
        criterio_parada = 0
    else:
        criterio_parada = criterio_parada + 1




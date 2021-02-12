import whois
dominio = "leveltwo.com.br"
consulta_whois = whois.whois(dominio)

#print (consulta_whois.email)
#print (consulta_whois["email"])
print (consulta_whois.text)

'''
Para instalar: baixe https://pypi.org/project/python-whois/
arraste para onde esta o python.exe e faca: python.exe setup.py install
'''

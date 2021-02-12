import time, msfrpc

client = msfrpc.Msfrpc({}) #cria o cliente que fara acesso do MSF via python
cliente.login("msf", "senha12345") #realiza o login no msfconsole
#load msgrpc Pass=senha12345
sessao = client.call("console.create") #cria um console dentro do msf passando as informacoes de ID para vinculo entre o comando python e o console criado
comando = """use auxiliary/scanner/smb/smb_version
set RHOSTS 10.0.0.100
exploit
""" #define o comando que e digitado no console

client.call("console.write", [sessao["id"], comando]) #escreve no console o comando
time.sleep(3) #aguarda 3 segundos para que seja executado o comando acima
resultado = client.call("console.read", [ sessao["id"] ]) #le o resultado

while resultado["busy"]:
    resultado = client.call("console.read", [sessao["id"]])
    time.sleep(1)

print resultado["data"]
client.call("console.destroy", [sessao["id"]]) #finaliza a sessao criada no MSFconsole

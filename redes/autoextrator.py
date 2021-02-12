import os, base64
arquivo1 =  raw_input("Arquivo 1: ")
arquivo2 =  raw_input("Arquivo 2: ")
nome_arquivo1 = os.path.basename(arquivo1)
nome_arquivo2 = os.path.basename(arquivo2)

with open (arquivo1, 'rb') as arquivo1_aberto:
    with open(arquivo2, 'rb') as arquivo2_aberto:
        with open('arquivo_final.py', 'w') as arquivo_criado:
            arquivo_criado.write('''import os, base64
            def join(conteudo_binario, nome_arquivo):
                if not os.path.exists(os.environ["TEMP"]+"\\\\"+nome_arquivo):
                    with open(os.environ["TEMP"]+"\\\\"+nome_arquivo,"wb") as arquivo_temporario:
                        arquivo_temporario.write(conteudo_binario)
                os.startfile(os.environ["TEMP"]+"\\\\"+nome_arquivo)
            arquivo1_base64 = "%s"
            join(base64.b64decode(arquivo1_base64), "%s")
            arquivo2_base64 = "%s"
            join(base64.b64decode(arquivo2_base64), "%s")
            '''%(base64.b64encode(arquivo1_aberto.read()),nome_arquivo1, \
                 base64.b64encode(arquivo2_aberto.read()), nome_arquivo2))

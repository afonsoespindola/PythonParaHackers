import ssl, socket
host = "maisinternet.tech"
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sockSSL = ssl.wrap_socket(sock)
sockSSL.connect((host,443))
sockSSL.send("HEAD / HTTP/1.1\r\nHost:%s\r\n\r\n" %host)
print sockSSL.recv(1024)
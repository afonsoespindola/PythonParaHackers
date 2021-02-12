with open("arquivo.txt", "w") as arquivo:
    arquivo.write("TEXTO")

arquivo.close()



with open("arquivo.txt", "w") as arquivo:
    arquivo.writelines("\n 0101")
arquivo.close()

with open("arquivo.txt", "r") as arquivo:
    print arquivo.read()
arquivo.close()
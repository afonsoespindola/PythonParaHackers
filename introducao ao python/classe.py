class Pessoa:
    def __init__(self, nome, sobrenome):
        self.nome = nome
        self.sobrenome = sobrenome

    def printar_nome_completo(self):
        return self.nome + " " + self.sobrenome

info_pessoa = Pessoa("Julia", "Souza")
print info_pessoa.printar_nome_completo()
print info_pessoa.nome + " " + info_pessoa.sobrenome

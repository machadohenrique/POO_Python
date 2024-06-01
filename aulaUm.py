# string = 'Henrique'
# print(string.upper())
# print(isinstance(string, str))


class Pessoa:
    def __init__(self, nome, sobrenome):
        self.nome = nome
        self.sobrenome = sobrenome



p1 = Pessoa('Gabriel','Henrique')
print(p1.nome)
print(p1.sobrenome)
# p1.nome = 'Gabriel'
# p1.sobrenome = 'Machado'
# print(p1.nome)
# print(p1.sobrenome)


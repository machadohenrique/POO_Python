#__dict__ e vars para atributos de instancia
class Pessoa:
    ano_atual = 2024

    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade
        
    
    def get_ano_nascimento(self):
        return Pessoa.ano_atual - self.idade

dados = {'nome': 'Joao', 'idade': 35}
p1 = Pessoa(**dados)

# p1 = Pessoa('Joao', 35)
# # p1.nome = 'EITAA'
# # p rint(p1.idade)
# print(p1.__dict__)
# print(vars(p1))

print(vars(p1))
print(p1.nome)
print(p1.idade)
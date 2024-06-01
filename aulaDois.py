# Classes é um molde para gerar novas instancias.
# Métodos em intancias de classes python
# Classe - Molde (geralmente sem dados)
# Instancia da class(objeto) - tem os dados
# Uma classe pode gerar várias instancias
# Na classe o self é a própria instacia.
class Carro:
    def __init__(self, nome):
        self.nome = nome
    
    def acelerar(self):
        print(f'{self.nome} esta acelerando...')



fusca = Carro('Fusca')
Carro.acelerar(fusca)
# print(fusca.nome)
# fusca.acelerar()

celta = Carro('Celta')
Carro.acelerar(celta)
# print(celta.nome)
# celta.acelerar()
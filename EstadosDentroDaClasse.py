class Camera:
    def __init__(self, nome, filmando = False):
        self.nome = nome
        self.filmando = filmando
    
    def filmar(self):
        if self.filmando:
            print(f'{self.nome} JA filmando')
            return
        
        print(f'{self.nome} está filmando')
        self.filmando = True
    
    def pararDeFilmar(self):
        if not self.filmando:
            print(f'{self.nome} nao esta filmando')
            return
        
        print(f'{self.nome} está parando de filmar')
        self.filmando = False  

    def fotografar(self):
        if self.filmando:
            print(f'{self.nome} nao pode fotografar')
            return
        
        print(f'{self.nome} está fotografando')


c1 = Camera('Canon')
c2 = Camera('Sony')
c1.filmar()
c1.filmar()
c1.fotografar()
c1.pararDeFilmar()
c1.fotografar()
# print(c1.filmando)
# print(c2.filmando)
print('-----------------------------')
c2.pararDeFilmar()
c2.filmar()
c2.filmar()
c2.fotografar()
c2.pararDeFilmar()
c2.fotografar()
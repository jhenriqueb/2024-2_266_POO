class Bicicleta:
    def __init__(self, veloc_atual=0, altura_cela=75, calibragem_pneus=30):
        self.veloc_atual = veloc_atual 
        self.altura_cela = altura_cela    
        self.calibragem_pneus = calibragem_pneus  

    def ajustar_velocidade(self, nova_velocidade):
        if nova_velocidade < 0:
            print("Velocidade não pode ser negativa.")
        else:
            self.veloc_atual = nova_velocidade

    def regular_cela(self, nova_altura):
        if self.veloc_atual == 0:
            if 50 <= nova_altura <= 100:
                self.altura_cela = nova_altura
            else:
                print("Altura da cela deve estar entre 50 e 100 cm.")
        else:
            print("A cela só pode ser ajustada quando a bicicleta está parada.")

    def calibrar_pneus(self, nova_calibragem):
        if self.veloc_atual == 0:
            if 25 <= nova_calibragem <= 50:
                self.calibragem_pneus = nova_calibragem
            else:
                print("Calibragem deve estar entre 25 e 50 PSI.")
        else:
            print("A calibragem dos pneus só pode ser feita quando a bicicleta está parada.")

    def mostrar_estado(self):
        return f"Velocidade Atual: {self.veloc_atual} km/h, Altura da Cela: {self.altura_cela} cm, Calibragem dos Pneus: {self.calibragem_pneus} PSI"

bicicleta = Bicicleta()

print(bicicleta.mostrar_estado())

bicicleta.regular_cela(80)
bicicleta.calibrar_pneus(35)

print(bicicleta.mostrar_estado())

bicicleta.ajustar_velocidade(10)
print("Após acelerar:")
print(bicicleta.mostrar_estado())

bicicleta.regular_cela(85)  
bicicleta.calibrar_pneus(40)  

bicicleta.ajustar_velocidade(0)

bicicleta.regular_cela(90)
bicicleta.calibrar_pneus(45)

print("Após ajustes com a bicicleta parada:")
print(bicicleta.mostrar_estado())

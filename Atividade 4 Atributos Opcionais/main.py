class Veiculo:
    def __init__(self, chassi, marca, modelo, ano, placa=None, cor="Não especificada", 
                 proprietario="Não especificado", quilometragem=0):
        
        self.chassi = chassi
        self.marca = marca
        self.modelo = modelo
        self.ano = ano
        
        self.placa = placa
        self.cor = cor
        self.proprietario = proprietario
        self.quilometragem = quilometragem

    def __str__(self):
        info = f"Chassi: {self.chassi}\n"
        info += f"Marca: {self.marca}\n"
        info += f"Modelo: {self.modelo}\n"
        info += f"Ano: {self.ano}\n"
        info += f"Placa: {self.placa if self.placa else 'Não especificada'}\n"
        info += f"Cor: {self.cor}\n"
        info += f"Proprietário: {self.proprietario}\n"
        info += f"Quilometragem: {self.quilometragem} km\n"
        return info

veiculo1 = Veiculo("1HGBH41JXMN109186", "Honda", "Civic", 2022, placa="ABC-1234", cor="Prata", proprietario="João Silva", quilometragem=15000)
veiculo2 = Veiculo("3N1AB7AP4FY345890", "Nissan", "Sentra", 2020)

print(veiculo1)
print(veiculo2)

from datetime import datetime

class CarteiraHabilitacao:
    CATEGORIAS_VALIDAS = ['A', 'B', 'C', 'D', 'E']
    
    def __init__(self, numero_cnh, nome, data_emissao, data_validade, categoria, endereco):
        self.numero_cnh = numero_cnh
        self.nome = nome
        self.data_emissao = self.validar_data_emissao(data_emissao)
        self.set_data_validade(data_validade)
        self.set_categoria(categoria)
        self.set_endereco(endereco)

    def validar_data_emissao(self, data_emissao):
        if isinstance(data_emissao, datetime) and data_emissao <= datetime.now():
            return data_emissao
        raise ValueError("Data de emissão inválida.")
    
    def set_data_validade(self, data_validade):
        if isinstance(data_validade, datetime) and data_validade > self.data_emissao:
            self.data_validade = data_validade
        else:
            raise ValueError("Data de validade inválida.")
    
    def set_categoria(self, categoria):
        if categoria in self.CATEGORIAS_VALIDAS:
            self.categoria = categoria
        else:
            raise ValueError(f"Categoria inválida.")
    
    def set_endereco(self, endereco):
        if isinstance(endereco, str) and endereco.strip():
            self.endereco = endereco
        else:
            raise ValueError("Endereço inválido.")
    
    def atualizar_endereco(self, novo_endereco):
        self.set_endereco(novo_endereco)
    
    def renovar_validade(self, nova_data_validade):
        self.set_data_validade(nova_data_validade)
    
    def atualizar_categoria(self, nova_categoria):
        self.set_categoria(nova_categoria)

    def __str__(self):
        return (f"CNH Nº: {self.numero_cnh}\nNome: {self.nome}\n"
                f"Data de Emissão: {self.data_emissao.strftime('%d/%m/%Y')}\n"
                f"Data de Validade: {self.data_validade.strftime('%d/%m/%Y')}\n"
                f"Categoria: {self.categoria}\nEndereço: {self.endereco}")

# Testando
try:
    data_emissao = datetime(2018, 5, 20)
    data_validade = datetime(2023, 5, 20)
    cnh1 = CarteiraHabilitacao("123456789", "João Silva", data_emissao, data_validade, "B", "Rua Exemplo, 123")
    print(cnh1)
    
    cnh1.atualizar_categoria("D")
    cnh1.renovar_validade(datetime(2028, 5, 20))
    cnh1.atualizar_endereco("Avenida Nova, 456")
    
    print("\nApós atualização:")
    print(cnh1)

except ValueError as e:
    print(f"Erro: {e}")

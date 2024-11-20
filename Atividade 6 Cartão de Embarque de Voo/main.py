import random
import string
from datetime import datetime, timedelta

class CartaoEmbarque:
    def __init__(self, nome_passageiro, numero_voo, codigo_reserva, data_hora_embarque):
        self.nome_passageiro = nome_passageiro
        self.numero_voo = numero_voo
        self.codigo_reserva = self._validar_codigo_reserva(codigo_reserva)
        self.data_hora_embarque = self._validar_data_hora_embarque(data_hora_embarque)
        
        self.status_checkin = False
        self.assento = None
        self.assentos_disponiveis = [f"{chr(row)}{col}" for row in range(65, 70) for col in range(1, 11)]

    def _validar_codigo_reserva(self, codigo):
        if len(codigo) == 6 and codigo.isalnum():
            return codigo
        raise ValueError("O código de reserva deve ter exatamente 6 caracteres alfanuméricos.")

    def _validar_data_hora_embarque(self, data_hora):
        if isinstance(data_hora, datetime) and data_hora > datetime.now():
            return data_hora
        raise ValueError("A data e hora do embarque devem ser futuras.")
    
    def realizar_checkin(self):
        if self.status_checkin:
            raise ValueError("O check-in já foi realizado.")
        if not self.assentos_disponiveis:
            raise ValueError("Não há assentos disponíveis.")
        
        self.status_checkin = True
        self.assento = random.choice(self.assentos_disponiveis)
        self.assentos_disponiveis.remove(self.assento)
        print(f"Check-in realizado com sucesso. Assento atribuído: {self.assento}.")

    def alterar_assento(self, novo_assento):
        if not self.status_checkin:
            raise ValueError("O check-in ainda não foi realizado.")
        if novo_assento not in self.assentos_disponiveis:
            raise ValueError("O assento solicitado não está disponível.")
        
        self.assentos_disponiveis.append(self.assento)
        self.assentos_disponiveis.remove(novo_assento)
        self.assento = novo_assento
        print(f"Assento alterado com sucesso para: {self.assento}.")

    def __str__(self):
        return (f"Cartão de Embarque\n"
                f"Nome do passageiro: {self.nome_passageiro}\n"
                f"Número do voo: {self.numero_voo}\n"
                f"Código da reserva: {self.codigo_reserva}\n"
                f"Data/Hora do embarque: {self.data_hora_embarque}\n"
                f"Status do check-in: {'Realizado' if self.status_checkin else 'Não realizado'}\n"
                f"Assento: {self.assento or 'Não atribuído'}")

if __name__ == "__main__":
    try:
        embarque1 = CartaoEmbarque("Ana Silva", "VOO123", "ABC123", datetime.now() + timedelta(hours=3))
        embarque2 = CartaoEmbarque("João Souza", "VOO456", "DEF456", datetime.now() + timedelta(days=1))
        embarque3 = CartaoEmbarque("Maria Oliveira", "VOO789", "GHI789", datetime.now() + timedelta(hours=5))

        print(embarque1)
        embarque1.realizar_checkin()
        print(embarque1)
        embarque1.alterar_assento("A2")
        print(embarque1)

        print(embarque2)
        embarque2.realizar_checkin()
        embarque2.alterar_assento("B4")
        print(embarque2)
        
    
    except Exception as e:
        print(f"Erro: {e}")

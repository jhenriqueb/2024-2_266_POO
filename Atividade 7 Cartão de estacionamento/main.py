import uuid
from datetime import datetime, timedelta

class CartaoEstacionamento:
    def __init__(self):
        self.__numero_cartao = str(uuid.uuid4().int)[:5]
        self.__data_hora_entrada = datetime.now()
        self.__status = "ativo"
        self.__data_hora_saida = None
        self.__valor_total = 0.0

    @property
    def numero_cartao(self):
        return self.__numero_cartao

    @property
    def data_hora_entrada(self):
        return self.__data_hora_entrada

    @property
    def status(self):
        return self.__status

    @property
    def data_hora_saida(self):
        return self.__data_hora_saida

    @property
    def valor_total(self):
        return self.__valor_total

    def registrar_saida(self):
        if self.__status != "ativo":
            raise ValueError("O cartão já está finalizado.")
        self.__data_hora_saida = datetime.now()
        if self.__data_hora_saida < self.__data_hora_entrada:
            raise ValueError("A data de saída não pode ser anterior à data de entrada.")
        self.__calcular_valor_total()
        self.__status = "finalizado"

    def consultar_valor_acumulado(self):
        if self.__data_hora_saida is None:
            return self.__calcular_valor_total(previsao=True)
        return self.__valor_total

    def __calcular_valor_total(self, previsao=False):
        saida = self.__data_hora_saida if not previsao else datetime.now()
        tempo_permanencia = saida - self.__data_hora_entrada
        minutos_totais = tempo_permanencia.total_seconds() / 60
        if minutos_totais <= 120:
            valor = 8.0
        else:
            minutos_extras = minutos_totais - 120
            fracoes = -(-minutos_extras // 15)
            valor = 8.0 + fracoes * 0.50
        if not previsao:
            self.__valor_total = valor
        return valor

    def __str__(self):
        saida = self.__data_hora_saida.strftime("%Y-%m-%d %H:%M:%S") if self.__data_hora_saida else "N/A"
        return (f"Cartão: {self.__numero_cartao}\n"
                f"Entrada: {self.__data_hora_entrada.strftime('%Y-%m-%d %H:%M:%S')}\n"
                f"Saída: {saida}\n"
                f"Status: {self.__status}\n"
                f"Valor Total: R$ {self.__valor_total:.2f}")


cartao1 = CartaoEstacionamento()
cartao2 = CartaoEstacionamento()
cartao3 = CartaoEstacionamento()

print("Cartão 1 - Entrada registrada")
print(cartao1)

print("\nConsultando valor acumulado para o Cartão 1 (ainda ativo):")
print(f"Valor acumulado: R$ {cartao1.consultar_valor_acumulado():.2f}")

print("\nRegistrando saída para o Cartão 1...")
cartao1.registrar_saida()
print(cartao1)

import time
time.sleep(2)

print("\nCartão 2 - Entrada registrada")
print(cartao2)

print("\nConsultando valor acumulado para o Cartão 2 (ainda ativo):")
print(f"Valor acumulado: R$ {cartao2.consultar_valor_acumulado():.2f}")

from typing import List
from dataclasses import dataclass
from enum import Enum

class TamanhoBebida(Enum):
    P = "P"
    M = "M"
    G = "G"

class ItemMenu:
    def __init__(self, nome: str, preco_base: float):
        self.nome = nome
        self.preco_base = preco_base

    def calcular_preco(self) -> float:
        return self.preco_base

class Prato(ItemMenu):
    def __init__(self, nome: str, preco_base: float, tempo_preparo: int):
        super().__init__(nome, preco_base)
        self.tempo_preparo = tempo_preparo

    def calcular_preco(self) -> float:
        return self.preco_base

class Bebida(ItemMenu):
    def __init__(self, nome: str, preco_base: float, tamanho: TamanhoBebida):
        super().__init__(nome, preco_base)
        self.tamanho = tamanho

    def calcular_preco(self) -> float:
        multiplicadores = {
            TamanhoBebida.P: 1.0,
            TamanhoBebida.M: 1.3,
            TamanhoBebida.G: 1.5
        }
        return self.preco_base * multiplicadores[self.tamanho]

@dataclass
class Cliente:
    nome: str

class Pedido:
    def __init__(self, cliente: Cliente, itens: List[ItemMenu]):
        self.cliente = cliente
        self.itens = itens

    def calcular_total(self) -> float:
        return sum(item.calcular_preco() for item in self.itens)

    def exibir_itens(self) -> str:
        resultado = f"\nCliente {self.cliente.nome} fez um pedido:"
        for item in self.itens:
            if isinstance(item, Prato):
                resultado += f"\n- Prato: {item.nome} (Tempo de preparo: {item.tempo_preparo} min) - R$ {item.calcular_preco():.2f}"
            elif isinstance(item, Bebida):
                resultado += f"\n- Bebida: {item.nome} (Tamanho: {item.tamanho.value}) - R$ {item.calcular_preco():.2f}"
        return resultado

class Mesa:
    def __init__(self, numero: int):
        self.numero = numero
        self.pedidos: List[Pedido] = []

    def registrar_pedido(self, cliente: Cliente, itens: List[ItemMenu]):
        pedido = Pedido(cliente, itens)
        self.pedidos.append(pedido)
        print(pedido.exibir_itens())

    def calcular_total(self) -> float:
        return sum(pedido.calcular_total() for pedido in self.pedidos)

    def imprimir_conta(self) -> str:
        resultado = f"\nResumo da mesa {self.numero}:"
        for pedido in self.pedidos:
            resultado += f"\n- {pedido.cliente.nome}: "
            itens_desc = []
            for item in pedido.itens:
                if isinstance(item, Prato):
                    itens_desc.append(f"{item.nome} (R$ {item.calcular_preco():.2f})")
                elif isinstance(item, Bebida):
                    itens_desc.append(f"{item.nome} {item.tamanho.value} (R$ {item.calcular_preco():.2f})")
            resultado += ", ".join(itens_desc)
        resultado += f"\nTotal: R$ {self.calcular_total():.2f}"
        return resultado

class Restaurante:
    def __init__(self):
        self.mesas: List[Mesa] = []

    def adicionar_mesa(self, numero: int):
        mesa = Mesa(numero)
        self.mesas.append(mesa)
        print(f"Cadastrando mesa {numero}...")
        return mesa

    def listar_mesas_ocupadas(self) -> List[Mesa]:
        return [mesa for mesa in self.mesas if mesa.pedidos]
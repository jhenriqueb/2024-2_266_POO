import pytest
from restaurante import Restaurante, Cliente, Prato, Bebida, TamanhoBebida

def test_criar_pedido():
    restaurante = Restaurante()
    mesa5 = restaurante.adicionar_mesa(5)
    
    joao = Cliente("João")
    hamburguer = Prato("Hambúrguer", 25.0, 15)
    refrigerante = Bebida("Refrigerante", 8.0, TamanhoBebida.G)
    
    mesa5.registrar_pedido(joao, [hamburguer, refrigerante])
    
    assert len(mesa5.pedidos) == 1
    assert mesa5.calcular_total() == 37.0  # 25.0 + (8.0 * 1.5)

def test_multiplos_pedidos_mesma_mesa():
    restaurante = Restaurante()
    mesa5 = restaurante.adicionar_mesa(5)
    
    joao = Cliente("João")
    hamburguer = Prato("Hambúrguer", 25.0, 15)
    refrigerante = Bebida("Refrigerante", 8.0, TamanhoBebida.G)
    mesa5.registrar_pedido(joao, [hamburguer, refrigerante])
    
    maria = Cliente("Maria")
    salada = Prato("Salada Caesar", 22.0, 10)
    suco = Bebida("Suco Natural", 10.0, TamanhoBebida.M)
    mesa5.registrar_pedido(maria, [salada, suco])
    
    assert len(mesa5.pedidos) == 2
    assert mesa5.calcular_total() == 72.0  # (25.0 + 8.0*1.5) + (22.0 + 10.0*1.3)

def test_bebida_diferentes_tamanhos():
    suco = Bebida("Suco", 10.0, TamanhoBebida.P)
    assert suco.calcular_preco() == 10.0
    
    suco_medio = Bebida("Suco", 10.0, TamanhoBebida.M)
    assert suco_medio.calcular_preco() == 13.0
    
    suco_grande = Bebida("Suco", 10.0, TamanhoBebida.G)
    assert suco_grande.calcular_preco() == 15.0

def test_listar_mesas_ocupadas():
    restaurante = Restaurante()
    mesa1 = restaurante.adicionar_mesa(1)
    mesa2 = restaurante.adicionar_mesa(2)
    
    joao = Cliente("João")
    hamburguer = Prato("Hambúrguer", 25.0, 15)
    mesa1.registrar_pedido(joao, [hamburguer])
    
    mesas_ocupadas = restaurante.listar_mesas_ocupadas()
    assert len(mesas_ocupadas) == 1
    assert mesas_ocupadas[0].numero == 1

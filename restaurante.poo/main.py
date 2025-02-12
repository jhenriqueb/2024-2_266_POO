from restaurante import Restaurante, Cliente, Prato, Bebida, TamanhoBebida

def main():
    restaurante = Restaurante()
    
    mesa5 = restaurante.adicionar_mesa(5)
    mesa7 = restaurante.adicionar_mesa(7)
    
    joao = Cliente("João")
    hamburguer = Prato("Hambúrguer", 25.0, 15)
    refrigerante = Bebida("Refrigerante", 8.0, TamanhoBebida.G)
    mesa5.registrar_pedido(joao, [hamburguer, refrigerante])

    maria = Cliente("Maria")
    salada = Prato("Salada Caesar", 22.0, 10)
    suco = Bebida("Suco Natural", 10.0, TamanhoBebida.M)
    mesa5.registrar_pedido(maria, [salada, suco])
    
    pedro = Cliente("Pedro")
    file = Prato("Filé Mignon", 55.0, 30)
    vinho = Bebida("Vinho Tinto", 40.0, TamanhoBebida.G)
    mesa7.registrar_pedido(pedro, [file, vinho])
    
    print("\nCalculando total da conta...")
    print(mesa5.imprimir_conta())
    print(mesa7.imprimir_conta())

if __name__ == "__main__":
    main()

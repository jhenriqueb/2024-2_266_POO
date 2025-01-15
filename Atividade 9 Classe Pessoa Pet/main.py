class Pet:
    def __init__(self, tipo, nome, idade, peso, raca, cor, castrado=False):
        self.__tipo = tipo
        self.__nome = nome
        self.__idade = idade
        self.__peso = peso
        self.__raca = raca
        self.__cor = cor
        self.__castrado = castrado

    @property
    def nome(self):
        return self.__nome

    def __str__(self):
        return f"{self.__nome} ({self.__tipo}, {self.__raca}, {self.__idade} anos, {self.__cor})"


class Pessoa:
    def __init__(self, cpf, nome, endereco):
        self.__cpf = cpf
        self.__nome = nome
        self.__endereco = endereco
        self.__meus_pets = []

    @property
    def cpf(self):
        return self.__cpf

    @property
    def nome(self):
        return self.__nome

    def cadastrar_pet(self, pet):
        self.__meus_pets.append(pet)
        print(f"Pet '{pet.nome}' cadastrado com sucesso para {self.__nome}.")

    def excluir_pet(self, nome):
        for pet in self.__meus_pets:
            if pet.nome == nome:
                self.__meus_pets.remove(pet)
                print(f"Pet '{nome}' removido com sucesso da lista de {self.__nome}.")
                return
        print(f"Pet '{nome}' não encontrado na lista de {self.__nome}.")

    def mostrar_meus_pets(self):
        if not self.__meus_pets:
            print(f"{self.__nome} não possui pets cadastrados.")
        else:
            print(f"Pets de {self.__nome}:")
            for pet in self.__meus_pets:
                print(f"  - {pet}")


if __name__ == "__main__":
    pessoa1 = Pessoa("12345678900", "Ana", "Rua A, 123")
    pessoa2 = Pessoa("98765432100", "Carlos", "Rua B, 456")
    pessoa3 = Pessoa("45612378900", "Beatriz", "Rua C, 789")

    pet1 = Pet("cachorro", "Rex", 3, 20.5, "Labrador", "amarelo", True)
    pet2 = Pet("gato", "Mimi", 2, 5.3, "SRD", "cinza", False)
    pet3 = Pet("cachorro", "Thor", 5, 25.0, "Pitbull", "marrom", True)
    pet4 = Pet("gato", "Felix", 1, 4.0, "SRD", "preto", False)

    pessoa1.cadastrar_pet(pet1)
    pessoa1.cadastrar_pet(pet2)
    pessoa2.cadastrar_pet(pet3)
    pessoa3.cadastrar_pet(pet4)

    pessoa1.mostrar_meus_pets()
    pessoa2.mostrar_meus_pets()
    pessoa3.mostrar_meus_pets()

    print("\n[Simulação de perda de pet]")
    pessoa1.excluir_pet("Mimi")

    print("\n[Após atualização]")
    pessoa1.mostrar_meus_pets()
    pessoa2.mostrar_meus_pets()
    pessoa3.mostrar_meus_pets()

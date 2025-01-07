class Pessoa:
    seq = 0

    def __init__(self, nome, idade, peso, altura, sexo, estado="vivo", est_civil="solteiro", mãe=None):
        Pessoa.seq += 1
        self.__id = Pessoa.seq

        self.__nome = nome
        self.__idade = idade
        self.__peso = peso
        self.__altura = altura
        self.__sexo = sexo
        self.__estado = estado
        self.__est_civil = est_civil
        self.__mãe = mãe
        self.__pai = None
        self.__mãe_adotiva = None
        self.__pai_adotivo = None
        self.__conjuge = None
        self.filhos = []

    @property
    def id(self):
        return self.__id

    @property
    def nome(self):
        return self.__nome

    @property
    def conjuge(self):
        return self.__conjuge

    @property
    def est_civil(self):
        return self.__est_civil

    @property
    def estado(self):
        return self.__estado

    @nome.setter
    def nome(self, valor):
        if self.__est_civil == "casado":
            nome_antigo = self.__nome.split(" ")
            nome_conjuge = self.__conjuge.nome.split(" ")
            novo_nome = valor.split(" ")
            for i in novo_nome:
                if (i not in nome_antigo) and (i not in nome_conjuge):
                    print("Nome inválido!")
                    return
            self.__nome = valor
            print("Alteração efetuada com sucesso!")

    def casar(self, conjuge):
        if self.estado == "morto" or conjuge.estado == "morto":
            print("Não é possível casar com uma pessoa morta!")
            return

        if type(conjuge) == Pessoa:
            if self.id != conjuge.id:
                if self.__est_civil in ["solteiro", "viúvo", "divorciado"] and conjuge.__est_civil in ["solteiro", "viúvo", "divorciado"]:
                    self.__est_civil = "casado"
                    self.__conjuge = conjuge
                    conjuge.__est_civil = "casado"
                    conjuge.__conjuge = self
                    print(f'{self.__nome} casou-se com {conjuge.nome}')
                else:
                    print("Um dos envolvidos já está casado!")
            else:
                print("Pessoa não pode se casar com ela mesma!")

    def morrer(self):
        if self.estado == "morto":
            print(f"{self.__nome} já está morto!")
            return
        self.__estado = "morto"
        if self.__est_civil == "casado":
            self.__conjuge.__est_civil = "viúvo"
            self.__conjuge.__conjuge = None
            print(f"{self.__nome} morreu e deixou {self.__conjuge.nome} viúvo(a).")
        else:
            print(f"{self.__nome} morreu.")

    def divorciar(self):
        if self.__est_civil == "casado":
            self.__conjuge.__est_civil = "divorciado"
            self.__conjuge.__conjuge = None
            self.__est_civil = "divorciado"
            self.__conjuge = None
            print(f"{self.__nome} se divorciou.")
        else:
            print("Não é possível se divorciar, pois a pessoa não está casada.")

    def ter_filhos(self, outra_pessoa):
        if self.estado == "morto" or outra_pessoa.estado == "morto":
            print("Um dos envolvidos está morto e não pode ter filhos.")
            return

        if self.__sexo == "F" and outra_pessoa.__sexo == "M":
            nome_filho = input("Digite o nome do filho: ")
            idade_filho = 0  # Bebê recém-nascido
            peso_filho = 3.5  # Peso médio ao nascer
            altura_filho = 0.5  # Altura média ao nascer
            filho = Pessoa(nome_filho, idade_filho, peso_filho, altura_filho, "F", mãe=self)
            filho.__pai = outra_pessoa
            self.filhos.append(filho)
            outra_pessoa.filhos.append(filho)
            print(f"{self.__nome} e {outra_pessoa.nome} tiveram um filho(a) chamado(a) {filho.nome}.")
            return filho
        else:
            print("Condições biológicas não atendidas para gerar filhos.")

    def __str__(self):
        return f"Nome: {self.__nome}, Idade: {self.__idade}, Estado Civil: {self.__est_civil}, Estado: {self.__estado}"


maria = Pessoa("Maria", 30, 65, 1.7, "F")  # Maria -> solteira
joao = Pessoa("João", 25, 66, 1.7, "M")    # João -> solteiro

maria.casar(joao)  # Maria e João -> casados
maria.morrer()     # Maria -> morta
joao.casar(maria)  # Não pode casar com uma pessoa morta
joao.divorciar()   # João -> viúvo, não divorciado
julia = joao.ter_filhos(maria)  # Não permitido, Maria está morta
ana = Pessoa("Ana", 22, 55, 1.6, "F")  # Ana -> solteira
filho = ana.ter_filhos(joao)  # Ana e João têm um filho

class Aluno:
    def __init__(self, nome):
        self.__nome = nome
        self.__nota1 = 0
        self.__nota2 = 0

    def definir_nome(self, nome):
        self.__nome = nome

    def get_nome(self):
        return self.__nome

    def definir_nota1(self, nota):
        if 0 <= nota <= 10:
            self.__nota1 = nota
        else:
            print("Nota inválida, deve ser entre 0 e 10")

    def get_nota1(self):
        return self.__nota1

    def definir_nota2(self, nota):
        if 0 <= nota <= 10:
            self.__nota2 = nota
        else:
            print("Nota inválida, deve ser entre 0 e 10")

    def get_nota2(self):
        return self.__nota2

    def calcular_media(self):
        return (self.__nota1 + self.__nota2) / 2

    def exibir_informacoes(self):
        print(f"{self.get_nome()} tem uma média de {self.calcular_media():.2f}")

aluno = Aluno("EDUARDO")
aluno.definir_nota1(6.2)
aluno.definir_nota2(5.5)
aluno.exibir_informacoes()

print(aluno.get_nome())
print(aluno.get_nota1())
print(aluno.get_nota2())

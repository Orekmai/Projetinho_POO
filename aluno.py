from datetime import datetime


class Aluno:
    def __init__(self, nome, data_nascimento, matricula, disciplinas):
        self.nome = nome
        self.data_nascimento = data_nascimento
        self.matricula = matricula
        self.disciplinas = disciplinas

    @property
    def idade(self):
        hoje = datetime.now()
        data_nasc = datetime.strptime(self.data_nascimento, '%d/%m/%Y')
        idade = hoje.year - data_nasc.year - ((hoje.month, hoje.day) < (data_nasc.month, data_nasc.day))
        return idade


    def lista(self):
        return ["matematica", "historia", "portugues", "geografia", "ingles"]

    def imprimir_info(self):
        print(f"Nome: {self.nome}")
        print(f"Matricula: {self.matricula}")
        print(f"Disciplinas: {', '.join(self.disciplinas)}")
         print(f"Idade: {self.idade}")


A1 = Aluno("Matheus", "1/1/2000", "2002", (lista)
A1.imprimir_info()

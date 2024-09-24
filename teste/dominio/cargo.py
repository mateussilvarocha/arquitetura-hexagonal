class Empregos:
    def __init__(self,nome, salario, fome, cansaco,):
       self.nome= nome
       self.salario= salario
       self.fome = fome
       self.cansaco= cansaco

    def usar(self, pessoa):
        pessoa.estado.fome += self.fome
        pessoa.estado.cansaco += self.cansaco
        pessoa.estado.saldo += self.salario


class Catador(Empregos):
    def __init__(self):
        super().__init__(nome='catador', salario=5, fome=10, cansaco=10)

class Frentista(Empregos):
    def __init__(self):
        super().__init__(nome='frentista', salario=5, fome=10, cansaco=15)

class ChefeGang(Empregos):
    def __init__(self):
        super().__init__(nome='chefe de Gangue', salario=10, fome=5, cansaco=20)

class CargoFactory:
    @staticmethod
    def criar_cargo(tipo_cargo):
        tipo_cargo = tipo_cargo.lower()
        if tipo_cargo == "catador":
            return Catador()
        elif tipo_cargo == "frentista":
            return Frentista()
        elif tipo_cargo == "chefeGang":
            return ChefeGang()
        else:
            raise ValueError(f"Cargo {tipo_cargo} não existe.")
        
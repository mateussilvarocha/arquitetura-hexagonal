class Comida:
    def __init__(self, nome, preco, fome, cansaco):
       self.nome= nome
       self.preco= preco
       self.fome= fome
       self.cansaco = cansaco

    def usar(self, pessoa):
        pessoa.estado.cansaco += self.cansaco 
        pessoa.estado.fome -= self.fome

    def comprar(self, pessoa):
        pessoa.estado.saldo -= self.preco

    def vender(self, pessoa):
        pessoa.estado.saldo += self.preco- (30/100)


class Comida_Estragada(Comida):
    def __init__(self):
        super().__init__(nome='comida_estragada', preco= 0, fome= 5, cansaco= 5)

class Comida_pobre(Comida):
    def __init__(self):
        super().__init__(nome='comida_pobre', preco=5, fome=5, cansaco = 0)

class Comida_rica(Comida):
    def __init__(self):
        super().__init__(nome='comida_rica', preco=10, fome=15, cansaco=0)

def filtro(tipo, gerenciador_eventos=None):
    if isinstance(tipo, str):
        return tipo.lower()
    else:
        gerenciador_eventos.tratar_evento('erro', {'mensagem': "Tipo errado."})

        
class ComidaFactory:
        
    @staticmethod
    def criar_comida(tipo_comida, gerenciador_eventos):
        tipo_comida = filtro(tipo_comida, gerenciador_eventos)

        if tipo_comida == "comida_estragada":
            return Comida_Estragada()
        elif tipo_comida == "comida_pobre":
            return Comida_pobre()
        elif tipo_comida == "comida_rica":
            return Comida_rica()
        else:
            raise ValueError(f"A comida {tipo_comida} não existe.")
        
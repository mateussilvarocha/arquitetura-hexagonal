class Casa:
    def __init__(self, nome, preco, bonus):
       self.nome= nome
       self.preco= preco
       self.bonus= bonus

    def comprar(self, pessoa):
        pessoa.estado.saldo -= self.preco

    def vender(self, pessoa):
        pessoa.estado.saldo += self.preco- (30/100)


class Nenhuma(Casa):
    def __init__(self):
        super().__init__(nome='nenhuma', preco=0, bonus=1)

class Casa_pobre(Casa):
    def __init__(self):
        super().__init__(nome='casa_pobre', preco=5, bonus=5)

class Casa_rica(Casa):
    def __init__(self):
        super().__init__(nome='casa_rica', preco=10, bonus=15)

def filtro(tipo, gerenciador_eventos=None):
    if isinstance(tipo, str):
        return tipo.lower()
    else:
        gerenciador_eventos.tratar_evento('erro', {'mensagem': "Tipo errado."})

        
class CasaFactory:
        
    @staticmethod
    def criar_casa(tipo_casa, gerenciador_eventos):
        tipo_casa = filtro(tipo_casa, gerenciador_eventos)

        if tipo_casa == "nenhuma":
            return Nenhuma()
        elif tipo_casa == "casa_pobre":
            return Casa_pobre()
        elif tipo_casa == "casa_rica":
            return Casa_rica()
        else:
            gerenciador_eventos.tratar_evento('erro', {'mensagem': f"Casa {tipo_casa} não existe."})

        

    
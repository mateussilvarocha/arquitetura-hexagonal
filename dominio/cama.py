class Cama:
    def __init__(self, nome, preco, fome, cansaco,):
       self.nome= nome
       self.preco= preco
       self.fome = fome
       self.cansaco= cansaco

    def usar(self, pessoa, bonus = 0):
        pessoa.estado.cansaco -= self.cansaco + bonus
        pessoa.estado.fome += self.fome

    def comprar(self, pessoa):
        pessoa.estado.saldo -= self.preco

    def vender(self, pessoa):
        pessoa.estado.saldo += self.preco- (30/100)


class Chao(Cama):
    def __init__(self):
        super().__init__(nome='chao', preco=5, fome=10, cansaco=15)

class Cama_pobre(Cama):
    def __init__(self):
        super().__init__(nome='cama_pobre', preco=5, fome=10, cansaco=15)

class Cama_rica(Cama):
    def __init__(self):
        super().__init__(nome='cama_rica', preco=10, fome=20, cansaco=25)

def filtro(tipo, gerenciador_eventos=None):
    if isinstance(tipo, str):
        return tipo.lower()
    else:
        gerenciador_eventos.tratar_evento('erro', {'mensagem': "Tipo errado."})

        
class CamaFactory:
    
        
    @staticmethod
    def criar_cama(tipo_cama, gerenciador_eventos):
        tipo_cama = filtro(tipo_cama, gerenciador_eventos)
        if tipo_cama == "chao":
            return Chao()
        elif tipo_cama == "cama_pobre":
            return Cama_pobre()
        elif tipo_cama == "cama_rica":
            return Cama_rica()
        else:
            gerenciador_eventos.tratar_evento('erro', {'mensagem': f"Cama {tipo_cama} não existe."})
        
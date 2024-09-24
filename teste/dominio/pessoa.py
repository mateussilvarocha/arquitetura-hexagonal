from dominio.cargo import CargoFactory
from dominio.cama import CamaFactory
from dominio.casa import CasaFactory
from dominio.comida import ComidaFactory
from componentes.listener import Subject
from dominio.eventos import Evento, GerenciadorEventos


class EstadoPessoa:
    def __init__(self):
        self._nome = ''
        self.endgame = False
        self._emprego = None
        self._saldo = 0
        self._fome = 0
        self._cansaco = 0

    @property
    def nome(self):
        return self._nome

    @nome.setter
    def nome(self, valor):
        self._nome = valor

    @property
    def emprego(self):
        return self._emprego

    @emprego.setter
    def emprego(self, valor):
        self._emprego = valor

    @property
    def saldo(self):
        return self._saldo

    @saldo.setter
    def saldo(self, valor):
        self._saldo = valor

    @property
    def fome(self):
        return self._fome

    @fome.setter
    def fome(self, valor):
        self._fome = valor

    @property
    def cansaco(self):
        return self._cansaco

    @cansaco.setter
    def cansaco(self, valor):
        self._cansaco = valor

    def atualizar_estado(self, estado_atualizado):
        """Atualiza o estado com base em um dicionário de dados"""
        for atributo, valor in estado_atualizado.items():
            setattr(self, atributo, valor)



class PartesCorpo:
    def __init__(self):
      
        self.cabeça=100
        self.braçodireito = 100
        self.braçoesquerdo = 100
        self.toraxe = 100
        self.pernadireita = 100
        self.pernaesquerda = 100
        

class Itens:
    def __init__(self):
    
        self.cama= None
        self.casa= None
        self.comida = None
        self.meioTransporte= 'pé'


class Pessoa(Subject):
    def __init__(self):
        super().__init__()
        self.estado = EstadoPessoa()
        self.partes_corpo = PartesCorpo()
        self.itens = Itens()
        self.eventos = Evento()
        self.gerenciador_eventos = GerenciadorEventos(self)
        self.eventos.adicionar_handler(self.gerenciador_eventos.tratar_evento)

    def mudar_nome(self, nome):
        self.eventos.notificar('nome_alterado', {'novo_nome': nome})

    def empregar(self, cargo):
        self.criar_cargo = CargoFactory.criar_cargo(cargo)

        try:
            self.eventos.notificar('cargo_alterado', {'novo_cargo': self.criar_cargo})
            if self.estado.emprego:
                self.eventos.notificar('cargo_alterado', {'novo_cargo': self.criar_cargo})

            else:
                self.eventos.notificar('erro', {"Erro: Emprego não atribuído."})

        except ValueError as e:
            self.eventos.notificar('erro', {'mensagem': str(e)})

        except AttributeError as e:
            self.eventos.notificar('erro', {'mensagem': f'Erro de atributo: {str(e)}'})

        except Exception as e:
            self.eventos.notificar('erro', {'mensagem': f'Ocorreu um erro: {str(e)}'})
             

    def comer(self, comida):
        self.itens.comida = ComidaFactory.criar_comida(comida)

        self.eventos.notificar('comeu', {'alimento': comida})

    def dormir(self, cama):
        if self.itens.casa is None :
            self.itens.casa = CasaFactory.criar_casa('nenhuma')
        
        self.itens.cama = CamaFactory.criar_cama(cama)

        #somar com o bonus da casa: casa = self.item['casa']
        self.eventos.notificar('dormiu', {'cama': cama})

    def trabalhar(self):
        try:
            if self.estado.emprego:
                self.eventos.notificar('trabalhou', {'novo_saldo': self.estado.saldo, 'fome': self.estado.fome, 'cansaco': self.estado.cansaco})
            else:
                self.eventos.notificar('erro', {'mensagem': 'Você ainda não tem um cargo.'})
        except Exception as e:
            self.eventos.notificar('erro', {'mensagem': str(e)})

    @property
    def saldo(self):
        return self.estado.saldo

    @saldo.setter
    def saldo(self, valor):
        self.estado.saldo = valor
        self.eventos.notificar('saldo_alterado', {'novo_saldo': self.estado.saldo})

    @property
    def fome(self):
        return self.estado.fome

    @fome.setter
    def fome(self, valor):
        self.estado.fome = valor
        self.eventos.notificar('fome_alterada', {'nova_fome': self.estado.fome})

    @property
    def cansaco(self):
        return self.estado.cansaco

    @cansaco.setter
    def cansaco(self, valor):
        self.estado.cansaco = valor
        self.eventos.notificar('cansaco_alterado', {'novo_cansaco': self.estado.cansaco})





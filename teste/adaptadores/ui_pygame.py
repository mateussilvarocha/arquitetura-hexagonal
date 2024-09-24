import pygame
from componentes.listener import LabelObserver
from adaptadores.utils_pygame.caixaoptions import CaixaDeOpcoes
from adaptadores.utils_pygame.button import ButtonFactory
from adaptadores.utils_pygame.label import LabelFactory

class Tela:
    def __init__(self, largura=1300, altura=600):
        pygame.init()
        self.largura = largura
        self.altura = altura
        self.tela = pygame.display.set_mode((self.largura, self.altura))
        pygame.display.set_caption("Pessoa")
        self.fonte = pygame.font.SysFont("Arial", 24)

    def desenhar(self):
        self.tela.fill((255, 255, 255)) 


class Elementos:
    def __init__(self, fonte, controlador, ui):
        self.ui = ui
        self.fonte = fonte
        self.controlador = controlador
        self.buttons = self.criar_buttons()
        self.caixas = self.criar_caixas()
        self.labels = self.criar_labels()

    def criar_buttons(self):
        dicionario_buttons = {
            'empregar': {
                'x': 100,
                'y': 200,
                'largura': 150,
                'altura': 50,
                'texto': 'Empregar',
                'cor': (241, 196, 15),
                'cor_hover': (243, 156, 18),
                'acao': lambda: self.controlador.empregar('Catador')
            },
            'trabalhar': {
                'x': 300,
                'y': 200,
                'largura': 150,
                'altura': 50,
                'texto': 'Trabalhar',
                'cor': (241, 196, 15),
                'cor_hover': (243, 156, 18),
                'acao': self.controlador.trabalhar
            },
            'exit': {
                'x': 100,
                'y': 300,
                'largura': 150,
                'altura': 50,
                'texto': 'Sair',
                'cor': (255, 0, 0),
                'cor_hover': (255, 100, 100),
                'acao': lambda: self.controlador.sair(self.ui)
            }
        }
        fabrica = ButtonFactory(self.fonte)
        return fabrica.criar_buttons(dicionario_buttons)

    def criar_caixas(self):
        opcoes = {
            "dormir": {
                'x': 0,
                'y': 0,
                'largura': 200,
                'altura': 30,
                'opcoes': [
                    {"nome": "No chão", "acao": lambda: self.controlador.dormir('chao')},
                    {"nome": "Cama pobre", "acao": lambda: self.controlador.dormir('cama pobre')},
                    {"nome": "Cama rica", "acao": lambda: self.controlador.dormir('cama rica')}
                ]
            },
            "comer": {
                'x': 220,
                'y': 0,
                'largura': 200,
                'altura': 30,
                'opcoes': [
                    {"nome": "Comida estragada", "acao": lambda: self.controlador.comer('comida_estragada')},
                    {"nome": "Comida pobre", "acao": lambda: self.controlador.comer('comida_pobre')},
                    {"nome": "Comida rica", "acao": lambda: self.controlador.comer('comida_rica')}
                ]
            }
        }

        caixas = [CaixaDeOpcoes(value['x'], value['y'], key, value['largura'], value['altura'], value['opcoes'], self.fonte)
                  for key, value in opcoes.items()]
        return caixas

    def criar_labels(self):
        dicionario_labels = {
            'saldo': {
                'x': 500,
                'y': 0,
                'texto': f'saldo: {self.controlador.saldo()}',
                'cor': (0, 0, 0)
            },
            'fome': {
                'x': 500,
                'y': 100,
                'texto': f'fome: {self.controlador.fome()}',
                'cor': (0, 0, 0)
            },
            'cansaco': {
                'x': 500,
                'y': 200,
                'texto': f'cansaço: {self.controlador.cansaco()}',
                'cor': (0, 0, 0)
            }
        }
        fabrica = LabelFactory(self.fonte)
        return fabrica.criar_labels(dicionario_labels)



        
class UIPygame:
    def __init__(self, pessoa):
        self.pessoa = pessoa
        self.controlador = ControladorPessoa(self.pessoa)
        self.tela = Tela()
        self.elementos = Elementos(self.tela.fonte, self.controlador, self)
        self.observador = LabelObserver
        self.configurar_observadores()

    def configurar_observadores(self):
        self.observador(self.pessoa, 'saldo', self.elementos.labels['saldo'])
        self.observador(self.pessoa, 'fome', self.elementos.labels['fome'])
        self.observador(self.pessoa, 'cansaco', self.elementos.labels['cansaco'])

    def checar_eventos(self, evento):
        if self.pessoa.estado.endgame is True:
            self.controlador.sair(self)

        for elemento in self.elementos.caixas:
            elemento.checar_evento(evento)

        for elemento in self.elementos.buttons.values():
            if hasattr(elemento, 'checar_evento'):
                elemento.checar_evento(evento)

    def desenhar(self):
        self.tela.desenhar()
        for label in self.elementos.labels.values():
            label.desenhar(self.tela.tela)

        for button in self.elementos.buttons.values():
            button.desenhar(self.tela.tela)

        for caixa in self.elementos.caixas:
            caixa.desenhar(self.tela.tela)

    def parar_execucao(self):
        self.rodando = False

    def executar(self):
        clock = pygame.time.Clock()
        self.rodando = True
        while self.rodando:
            self.desenhar()
            for evento in pygame.event.get():
                if evento.type == pygame.QUIT:
                    self.rodando = False
                self.checar_eventos(evento)

            pygame.display.flip()
            clock.tick(60)

        pygame.quit()


#---- actions ----
class ControladorPessoa:
    def __init__(self, pessoa):
        self.controlador = pessoa

    def comer(self, item):
        self.controlador.comer(item)

    def saldo(self):
        return self.controlador.saldo

    def fome(self):
        return self.controlador.fome

    def cansaco(self):
        return self.controlador.cansaco

    def empregar(self, trabalho):
        self.controlador.empregar(trabalho)

    def dormir(self, lugar):
        self.controlador.dormir(lugar)

    def trabalhar(self):
        self.controlador.trabalhar()

    def sair(self, ui):
        ui.parar_execucao()




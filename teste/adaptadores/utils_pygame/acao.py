class Acao:
    def __init__(self, id_button):
        self.id_button= id_button
        self.ids = {'run': self.jogar, 'exit': self.sair}

    def executar(self):

    def jogar(self):
        print("jogar clicado")

    def sair(self):
        print("Sair clicado")  # Ação do botão "Sair"
        self.rodando = False
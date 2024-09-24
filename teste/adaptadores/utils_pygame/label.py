


class Label:
    def __init__(self, x, y, texto, cor, fonte):
        self.x = x
        self.y = y
        self.texto = texto
        self.cor = cor
        self.fonte = fonte  # Deve ser um objeto pygame.font.Font

    def desenhar(self, tela):
        texto_surface = self.fonte.render(self.texto, True, self.cor)
        tela.blit(texto_surface, (self.x, self.y))
# componentes/button.py


class LabelFactory:
    def __init__(self, fonte):
        self.fonte = fonte
        self.labels = {}

    def criar_labels(self, dicionario_labels):
        
        for key, item in dicionario_labels.items():
            # Cria o botão usando os valores do dicionário
            label = Label(
                x=item['x'],
                y=item['y'],
                texto=item['texto'],
                cor=item['cor'],
                fonte=self.fonte
            )
            self.labels[key]=label

        return self.labels



# componentes/button.py
import pygame

class ButtonFactory:
    def __init__(self, fonte):
        self.fonte = fonte
        self.buttons = {}

    def criar_buttons(self, dicionario_buttons):
        """
        Cria botões com as especificações fornecidas.

        :param dicionario_buttons: Lista de dicionários onde cada dicionário contém as especificações do botão
        :return: Lista de instâncias do Button
        """
        for key, item in dicionario_buttons.items():
            # Cria o botão usando os valores do dicionário
            botao = Button(
                x=item['x'],
                y=item['y'],
                largura=item['largura'],
                altura=item['altura'],
                texto=item['texto'],
                cor=item['cor'],
                cor_hover=item['cor_hover'],
                fonte=self.fonte,
                acao=item['acao']
            )
            self.buttons[key]=botao

        return self.buttons

   
        """
        Cria um botão com as especificações fornecidas.

        :param x: Posição x do botão
        :param y: Posição y do botão
        :param largura: Largura do botão
        :param altura: Altura do botão
        :param texto: Texto a ser exibido no botão
        :param cor: Cor padrão do botão
        :param cor_hover: Cor do botão quando o mouse está sobre ele
        :param acao: Função a ser executada quando o botão é clicado
        :return: Instância do Button
        """     
class Button:
    def __init__(self, x, y, largura, altura, texto, cor, cor_hover, fonte, acao=None):
        # Definindo os atributos da classe
        self.rect = pygame.Rect(x, y, largura, altura)
        self.texto = texto
        self.cor = cor
        self.cor_hover = cor_hover
        self.fonte = fonte
        self.acao = acao  # Função a ser executada quando o botão é clicado
        self.hovered = False  # Estado de hover do botão

    def desenhar(self, tela):
        # Altera a cor do botão com base no estado de hover
        cor_atual = self.cor_hover if self.hovered else self.cor
        pygame.draw.rect(tela, cor_atual, self.rect)
        texto_surface = self.fonte.render(self.texto, True, (0, 0, 0))
        tela.blit(texto_surface, (self.rect.x + (self.rect.width - texto_surface.get_width()) // 2,
                                  self.rect.y + (self.rect.height - texto_surface.get_height()) // 2))

    def checar_evento(self, evento):
        # Checa se o mouse está sobre o botão
        if evento.type == pygame.MOUSEMOTION:
            self.hovered = self.rect.collidepoint(evento.pos)
        # Checa se o botão foi clicado
        if evento.type == pygame.MOUSEBUTTONDOWN and (self.rect.collidepoint(evento.pos) and self.acao):
            self.acao()

import pygame

class CaixaDeOpcoes:
    def __init__(self, x, y, nome_caixa, largura, altura, opcoes, fonte, cor_caixa=(0, 0, 255), cor_opcao=(0, 255, 0), cor_texto=(255, 255, 255)):
        self.x = x
        self.y = y
        self.nome_caixa = nome_caixa
        self.largura = largura
        self.altura = altura
        self.opcoes = opcoes  # Lista de dicionários {'nome': 'Descrição', 'acao': funcao}
        self.caixa_aberta = False
        self.selecionado = None
        self.fonte = fonte
        self.cor_caixa = cor_caixa
        self.cor_opcao = cor_opcao
        self.cor_texto = cor_texto
        self.altura_item = altura

    def desenhar(self, tela):
        pygame.draw.rect(tela, self.cor_caixa, (self.x, self.y, self.largura, self.altura))
        texto = self.fonte.render(self.nome_caixa, True, self.cor_texto)
        tela.blit(texto, (self.x + 10, self.y + 5))

        if self.caixa_aberta:
            for i, opcao in enumerate(self.opcoes):
                pygame.draw.rect(tela, self.cor_opcao, (self.x, self.y + self.altura + i * self.altura_item, self.largura, self.altura_item))
                texto_opcao = self.fonte.render(opcao['nome'], True, self.cor_texto)
                tela.blit(texto_opcao, (self.x + 10, self.y + self.altura + i * self.altura_item + 5))

    def checar_evento(self, evento):
        if evento.type == pygame.MOUSEBUTTONDOWN:
            mouse_x, mouse_y = evento.pos

            # Verifica se clicou na caixa principal
            if self.x <= mouse_x <= self.x + self.largura and self.y <= mouse_y <= self.y + self.altura:
                self.caixa_aberta = not self.caixa_aberta

            # Verifica se a caixa está aberta e o usuário clicou em uma das opções
            if self.caixa_aberta:
                for i, opcao in enumerate(self.opcoes):
                    if (self.x <= mouse_x <= self.x + self.largura and
                        self.y + self.altura + i * self.altura_item <= mouse_y <= self.y + self.altura + (i + 1) * self.altura_item):
                        opcao['acao']()
                          # Armazena a função 'acao'
                        self.caixa_aberta = False  # Fecha a caixa depois da seleção

    
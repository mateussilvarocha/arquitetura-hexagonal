

# adaptadores/ui_terminal.py



class UITerminal:
    def __init__(self, pessoa):
        self.pessoa = pessoa
        self.listener = pessoa.listener

    def executar(self):
        self.pessoa.mudar_nome('Mateus')
        # Escolhe um emprego
        self.pessoa.empregar('ChefeGang')

        # Mostra todas as mensagens capturadas até o momento
        self.listener.mostrar_logs()

        self.pessoa.comer('a')
        self.pessoa.dormir('a')
    
        self.pessoa.trabalhar()
        self.pessoa.trabalhar()
        self.pessoa.empregar('Catador')
        self.pessoa.trabalhar()
        self.pessoa.trabalhar()
        # trabalhar('catador')
        # trabalhar('catador')
        # trabalhar('catador')
        # print(pessoa)
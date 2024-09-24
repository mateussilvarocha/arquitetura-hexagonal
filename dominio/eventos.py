import traceback


class GerenciadorEventos:
    def __init__(self, pessoa):
        self.pessoa = pessoa
        self.event_map = {
            'nome_alterado': self.tratar_nome_alterado,
            'cargo_alterado': self.tratar_cargo_alterado,
            'comeu': self.tratar_comeu,
            'dormiu': self.tratar_dormiu,
            'trabalhou': self.tratar_trabalhou,
            'erro': self.tratar_erro,
            'saldo_alterado': self.tratar_saldo_alterado,
            'fome_alterada': self.tratar_fome_alterada,
            'cansaco_alterado': self.tratar_cansaco_alterado,
        }

    def tratar_evento(self, tipo_evento, dados):
        
        handler = self.event_map.get(tipo_evento)
        if handler:
            handler(dados)
            self.tratar_endgame()
            self.pessoa.notificar_observadores()

        else:
            print(f"Evento não reconhecido: {tipo_evento}")
        

    def tratar_nome_alterado(self, dados):
        print(dados)
        self.pessoa.estado.nome = dados['novo_nome'] #recebe uma string: 'Nome'

        print(f"Nome alterado para {dados['novo_nome']}")

    def tratar_cargo_alterado(self, dados):
        #print(dados) ==> {'novo_cargo': <dominio.cargo.Catador object at 0x0000023905390190>}

        self.pessoa.estado.emprego = dados['novo_cargo'] # recebe um class
        print(f"Cargo alterado para {dados['novo_cargo'].nome}")

    def tratar_comeu(self, dados):
        self.pessoa.itens.comida.usar(self.pessoa)

        print(f"{self.pessoa.estado.nome} comeu {dados['alimento']}")

    def tratar_dormiu(self, dados):
        
        if self.pessoa.itens.cama is not None and self.pessoa.itens.casa is not None:
            self.pessoa.itens.cama.usar(self.pessoa, self.pessoa.itens.casa.bonus)
            print(f"{self.pessoa.estado.nome} dormiu em uma {dados['cama']}")
        else:
            # Notifica um erro se a cama for None
            self.tratar_erro({'mensagem': "Erro: Nenhuma cama foi atribuída."})
    
    def tratar_trabalhou(self, dados):
        emprego = self.pessoa.estado.emprego
        emprego.usar(self.pessoa)
        print(f"{self.pessoa.estado.nome} trabalhou. Novo saldo: {dados['novo_saldo']}, Fome: {dados['fome']}, Cansaço: {dados['cansaco']}")


    def tratar_saldo_alterado(self, dados):
        print(f"Saldo alterado para {dados['novo_saldo']}")

    def tratar_fome_alterada(self, dados):
        print(f"Fome alterada para {dados['nova_fome']}")

    def tratar_cansaco_alterado(self, dados):
        print(f"Cansaço alterado para {dados['novo_cansaco']}")

    def tratar_erro(self, dados):
        # Captura o rastreamento de pilha (stack trace)
        erro = dados['mensagem']
        linha_erro = traceback.format_exc()
        
        # Exibe a mensagem de erro e a linha correspondente
        print(f"Erro: {erro}")
        print(f"Detalhes do erro:\n{linha_erro}")

    def tratar_endgame(self):
        if self.pessoa.estado.fome >= 100 or self.pessoa.estado.cansaco >= 100:
            self.pessoa.estado.endgame = True
            print('você morreu')
        

class Evento:
    def __init__(self):
        self.handlers = []

    def adicionar_handler(self, handler):
        self.handlers.append(handler)

    def remover_handler(self, handler):
        self.handlers.remove(handler)

    def notificar(self, tipo_evento, dados=None):
        for handler in self.handlers:
            handler(tipo_evento, dados)


if __name__ == "__main__":
    
    from dominio.pessoa import Pessoa
    # Exemplo de uso
    pessoa = Pessoa()
    gerenciador_eventos = GerenciadorEventos(pessoa)
    pessoa.adicionar_observador(gerenciador_eventos.tratar_evento)



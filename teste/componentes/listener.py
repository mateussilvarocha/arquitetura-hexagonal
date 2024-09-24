
class Subject:
    def __init__(self):
        self._observadores = []

    def adicionar_observador(self, observador):
        self._observadores.append(observador)

    def remover_observador(self, observador):
        self._observadores.remove(observador)

    def notificar_observadores(self):
        for observador in self._observadores:
            observador.atualizar()


class Observador:
    def atualizar(self, evento):
        raise NotImplementedError("A classe filha deve implementar esse método")
    

class Listener():
    def __init__(self):
        self.logs = []
    
    def ouvir(self, mensagem):
        """Recebe a mensagem e armazena no log"""
        self.logs.append(mensagem)
        print(f"Ouvindo: {mensagem}")  # Aqui você pode substituir por outra lógica de output, como salvar em arquivo.

    def mostrar_logs(self):
        """Exibe todas as mensagens ouvidas até agora"""
        print("\n--- Log de Mensagens ---")
        for log in self.logs:
            print(log)


class LabelObserver(Observador):
    
    def __init__(self, pessoa, atributo, label_elemento):
        self.pessoa = pessoa
        self.atributo = atributo
        self.label_elemento = label_elemento
        self.pessoa.adicionar_observador(self)

    def ouvir(self, mensagem):
        """Recebe a mensagem e armazena no log"""
        self.logs.append(mensagem)
        
    def atualizar(self):
        valor_atualizado = getattr(self.pessoa, self.atributo)
        self.label_elemento.texto = f"{self.atributo}: {valor_atualizado}"




from dominio.pessoa import Pessoa
from adaptadores.ui_terminal import UITerminal
from adaptadores.ui_pygame import UIPygame

if __name__ == "__main__":
    
    pessoa = Pessoa()

    # Inicializa a interface com Pygame
    ui = UIPygame(pessoa)

    ui.executar()

# if __name__ == "__main__":
#     listener = Listener()
#     pessoa = Pessoa(listener)

#     # Inicializa a interface com Pygame
#     ui = UITerminal(pessoa)
#     ui.executar()
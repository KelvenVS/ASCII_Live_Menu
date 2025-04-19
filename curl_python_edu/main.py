import os

def limpar_cmd():
    """Função para limpar o terminal."""
    os.system('cls') if os.name == 'nt' else  os.system('clear')
    
def get_ascii(art_name):
    """Faz uma requisição ao ASCII Live para exibir arte."""
    command = f"curl http://ascii.live/{art_name}"
    os.system(command)

class Menu:
    def __init__(self):
        self.menu_dict = {
            "batman": lambda: get_ascii("batman"),
            "can-you-hear-me": lambda: get_ascii("can-you-hear-me"),
            "hes": lambda: get_ascii("hes"),
            "knot": lambda: get_ascii("knot"),
            "bnr": lambda: get_ascii("bnr"),
            "coin": lambda: get_ascii("coin"),
            "donut": lambda: get_ascii("donut"),
            "parrot": lambda: get_ascii("parrot"),
            "spidyswing": lambda: get_ascii("spidyswing"),
            "dvd": lambda: get_ascii("dvd"),
            "playstation": lambda: get_ascii("playstation"),
            "batman-running": lambda: get_ascii("batman-running"),
            "clock": lambda: get_ascii("clock"),
            "forrest": lambda: get_ascii("forrest"),
            "nyan": lambda: get_ascii("nyan"),
            "rick": lambda: get_ascii("rick"),
            "torus-knot": lambda: get_ascii("torus-knot")
        }

    def safe_input(self, data_type, prompt):
        """Função para validar entradas do usuário."""
        while True:
            try:
                return data_type(input(prompt))
            except ValueError:
                print(f"Entrada inválida! Digite um valor do tipo {data_type.__name__}.")

    def exibir_menu(self):
        """Exibe o menu e captura a opção escolhida pelo usuário."""
        menu_keys = list(self.menu_dict.keys())

        while True:
            print(f"\n{'#'*47} Menu {'#'*47}")
            for i, elem in enumerate(menu_keys, 1):
                print(f"{i}. {elem}")
            print(f"{'#'*100}") 

            option = self.safe_input(int, "Escolha uma das opções: ")

            if option not in range(1, len(menu_keys) + 1):
                print("Opção inválida, tente novamente.")
            else:
                self.menu_dict[menu_keys[option - 1]]()

if __name__ == '__main__':
    menu = Menu()
    menu.exibir_menu()
from os import system
from termcolor import colored

class AntialiasingView:
    def start_view(self):
        system('cls')
    print(colored("**Prtojeto Anti-aliasing**\n", 'blue'))
    
    def ask_directory(self):
        path = input(
            colored(
                'Em qual diretório deseja aplicar o efeito nos arquivos?\n', 'cyan'
            )
        )
        return path
    
    def ask_anti_aliasing_method(self):
        system('cls')
        method = input(
            colored(
                "Qual método deseja utilizar?\n 1 para Hanning\n 2 para Lanczos\n", 'cyan'
            )
        )
        
        is_hanning = method =='1'
        method_name = "hanning" if is_hanning else "lanczos"
        
        return method_name
        
    def print_request_infos(self, method, files):
        system('cls')
        print(
            colored(
                f"Aplicando método {method} nos arquivos: ", 'blue'
            )
        )
        
        for index in range(len(files)):
            print(
            
            colored(f"      arquivo {index}: '{files[index]}'", 'cyan')
        )
        
    def ask_want_to_continue(self):
        system('cls')
        choice = input(
            colored("Deseja continuar?\n y para continuar \n n para finalizar\n", 'cyan')
        )
        return choice
            
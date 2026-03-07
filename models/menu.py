class Menu:
    def __init__(self):
        pass

    def exibir_opcoes(self):
        
        print("\n[MENU DE SERVIÇOS]")
        print("1. Consulta")
        print("2. Exame")
        print("3. Emergência")
        
        escolha = input("Escolha a opção: ")
        return escolha # 
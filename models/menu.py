class Menu: 
    def exibir_opcoes(self):
        print("\n[MENU DE SERVIÇOS]")
        print("1. Consulta")
        print("2. Exame")
        print("3. Emergência")
        
    def obter_escolha(self):
        return input("Escolha a opção: ")
    
class Menu: 
    def exibir_opcoes (self):
        print("\n--- Sistema de Gestão de Pacientes ---")
        print("1. Cadastrar Paciente")
        print("2. Ver Lista de Pacientes")
        print("3. Sair")
        
    def obter_escolha(self):
        return input("Escolha o serviço desejado: ")
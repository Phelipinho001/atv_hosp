from datetime import datetime

class Impressora:
<<<<<<< Updated upstream
<<<<<<< Updated upstream
    @staticmethod
    def imprimir_ticket(paciente, servico, senha=None):
        """
        Gera um ticket visualmente organizado no console.
        """
        data_atual = datetime.now().strftime("%d/%m/%Y %H:%M:%S")
        
        print("-" * 30)
        print(f"{'HOSPITAL GEMINI':^30}")
        print("-" * 30)
        print(f"Data: {data_atual}")
        print(f"Paciente: {paciente.nome}")
        print(f"Serviço: {servico}")
        
        if senha:
            print(f"\nSENHA: {senha}")
        else:
            print("\nSTATUS: ATENDIMENTO IMEDIATO")
            
        print("-" * 30)
        print(f"{'Mantenha este ticket':^30}")
        print("-" * 30)
=======
=======
>>>>>>> Stashed changes
    def __init__(self):
        pass

    def imprimir_ticket(self, paciente, tipo, servico, senha):
        """
        Recebe os 4 argumentos enviados pela main e imprime o ticket formatado.
        """
        data_atual = datetime.now().strftime("%d/%m/%Y %H:%M:%S")
        
        print("\n" + "-" * 42)
        print(f"{'TICKET DE ATENDIMENTO':^42}")
        print("-" * 42)
        print(f"PACIENTE: {paciente.nome}")
        print(f"TIPO: {tipo}")
        print(f"SERVIÇO: {servico}")
        print(f"SENHA: {senha}")
        print("-" * 42)
        print(f"Data: {data_atual}")
        print(f"{'Aguarde ser chamado no painel central.':^42}")
<<<<<<< Updated upstream
        print("-" * 42 + "\n")
>>>>>>> Stashed changes
=======
        print("-" * 42 + "\n")
>>>>>>> Stashed changes

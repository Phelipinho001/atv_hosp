from datetime import datetime

class Impressora:
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
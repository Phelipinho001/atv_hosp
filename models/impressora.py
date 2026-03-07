from datetime import datetime

class Impressora:
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
        print("-" * 42 + "\n")

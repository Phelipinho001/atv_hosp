class Triagem:
    def __init__(self):
        self.ALERTA_CRITICO = "CASO URGENTE"

    def filtrar_fluxo(self, escolha_paciente):

        if escolha_paciente.strip().lower() in ["emergencia", "emergência", "1"]:
            print(f"\n{"!"*40}")
            print(f"ALERTA: {self.ALERTA_CRITICO}")
            print(f"{"!"*40}\n")
            return True
        
        return False
    
    def exibir_alerta_emergencia(self, paciente):
        print("\n------------------------------------------")
        print("ALERTA DE EMERGÊNCIA")
        print("------------------------------------------")
        print(f"PACIENTE: {paciente.nome}")
        print("STATUS: RISCO IMEDIATO")
        print(">>> ATENÇÃO: Encaminhe-se IMEDIATAMENTE")
        print("ao balcão de triagem médica.")
        print("Não é necessário aguardar senha.")
        print("------------------------------------------")

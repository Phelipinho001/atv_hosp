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

from models.paciente import Pacient

class Classificador():
    @staticmethod
    def classificar(paciente: Pacient):
        
        if paciente.pcd == True or paciente.idade >= 60:
            return "PRIORITÁRIO (Lei 10.048)"
        else:
            return "Geral"


classificar = Classificador.classificar

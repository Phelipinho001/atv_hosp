from paciente import Pacient

class Classificador():

    @staticmethod

    def classificar(Paciente : Pacient):
        if Paciente.pcd.upper() == "S" or Paciente.idade >=60:
            return "Prioridade"
        
        else:
            return "Normal"
        
classificar = Classificador.classificar

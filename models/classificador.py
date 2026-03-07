from models.paciente import Pacient

class Classificador():

    @staticmethod

    def classificar(Paciente : Pacient):
        if Paciente.pcd == True or Paciente.idade >=60:
            return "PRIORITÁRIO (Lei 10.048)"
        
        else:
            return "Normal"
        
classificar = Classificador.classificar


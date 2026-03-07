from models.paciente import Pacient

class Classificador():

    @staticmethod

    def classificar(Paciente : Pacient):
        if Paciente.pcd == True or Paciente.idade >=60:
<<<<<<< Updated upstream
<<<<<<< Updated upstream
            return "PRIORITÁRIO (Lei 10.048)"
=======
=======
>>>>>>> Stashed changes
            return "Prioridade"
>>>>>>> Stashed changes
        
        else:
            return "Normal"
        
classificar = Classificador.classificar

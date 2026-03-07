from models.paciente import Pacient
from models.menu import Menu
from models.classificador import Classificador
from models.senha import Senha
from models.triagem import Triagem
from models.impressora import Impressora

def rodar_totem():
<<<<<<< Updated upstream
    
=======
>>>>>>> Stashed changes
    Paciente = Pacient
    menu = Menu()
    classificador = Classificador()
    gerador_senha = Senha()
    triagem = Triagem()
    impressora = Impressora()

    while True:
        print("\n==========================================")
        print("HOSPITAL VIVER BEM - AUTOATENDIMENTO")
        print("==========================================")

        print("\n[CADASTRO DE PACIENTE]")
        nome = input("Nome: ")
<<<<<<< Updated upstream
        if nome.upper() == "SAIR": 
            print("Encerrando sistema...")
            break
=======
        if nome.upper() == "SAIR": break
>>>>>>> Stashed changes
        
        try:
            idade = int(input("Idade: "))
            pcd_input = input("Possui deficiência? (S/N): ").strip().upper()
            pcd = True if pcd_input == 'S' else False
            
            
            paciente = Paciente(nome, idade, pcd)

<<<<<<< Updated upstream
           
            menu.exibir_opcoes()
            servico_escolhido = menu.obter_escolha()
=======
            
            servico_escolhido = menu.exibir_opcoes()

          
           
>>>>>>> Stashed changes

            if servico_escolhido == "3":
               
                triagem.exibir_alerta_emergencia(paciente)
            else:
<<<<<<< Updated upstream
               
                tipo_atendimento = classificador.classificar(paciente)
                senha_gerada = gerador_senha.gerador_senha(tipo_atendimento)
                
                nome_servico = "Consulta" if servico_escolhido == "1" else "Exame"
                
            
                impressora.imprimir_ticket(paciente, tipo_atendimento, nome_servico, senha_gerada)
=======
                
                tipo_atendimento = classificador.classificar(paciente)
                senha = gerador_senha.gerador_senha(tipo_atendimento)
                
                nome_servico = "Consulta" if servico_escolhido == "1" else "Exame"
                
                impressora.imprimir_ticket(paciente, tipo_atendimento, nome_servico, senha)
>>>>>>> Stashed changes

            print("\n" + "."*40)
            input("Sistema pronto para o próximo paciente. Aperte ENTER.")

        except ValueError:
<<<<<<< Updated upstream
            print("\n[ERRO] Idade deve ser um número. Reinicie o cadastro.")
=======
            print("\n[ERRO] Entrada inválida. Por favor, reinicie o cadastro.")
>>>>>>> Stashed changes

if __name__ == "__main__":
    rodar_totem()
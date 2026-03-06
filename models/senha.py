
class Senha:
    senha_prioridade = 0
    senha_geral = 0
    
    
    def gerador_senha(cls, tipo : str) -> str : 
        if tipo == "Prioridade":
            cls.senha_prioridade += 1 
            numero = str(cls.senha_prioridade).zfill(3)
            return f"P-{numero}"
    
        else:
            cls.senha_geral +=1
            numero = str(cls.senha_geral).zfill(3)
            return f"G-{numero}"
        
gerador_senha = Senha.gerador_senha
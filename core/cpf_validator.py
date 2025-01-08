from utils.format_cpf import validar_formato_cpf
from .cpf_generator import calcular_digito_verificador

def validar_cpf(cpf):
    try:
        cpf = validar_formato_cpf(cpf)
        
        nove_digitos = cpf[:9]
        primeiro_digito = calcular_digito_verificador(nove_digitos, 10)
        segundo_digito = calcular_digito_verificador(nove_digitos+primeiro_digito, 11)
        
        verificar_cpf = f"{nove_digitos}{primeiro_digito}{segundo_digito}"
        
        return verificar_cpf == cpf # Se é True ou False
    
    except ValueError as e:
        print(f"Erro de validação: {e}")
        return False
    except Exception as e:
        return f"Erro inesperado: {e}"
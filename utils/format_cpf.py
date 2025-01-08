import re

def validar_formato_cpf(cpf):
    cpf = str(cpf)
    # cpf = cpf.replace(".","")
    # cpf = cpf.replace("-","")
    cpf = re.sub(r'\D', '', cpf)
    
    if not cpf.isdigit():
        raise ValueError("Favor digite apenas NÚMEROS.")
    
    if len(cpf) != 11:
        raise  ValueError("O CPF deve conter 11 digitos") 

    if cpf == cpf[0] * len(cpf):
        raise ValueError(f"O CPF: {cpf} não é válido (Sequência repetida)")
    
    return cpf

def cpf_formatado(cpf):
    try:
        validar_formato_cpf(cpf)

        # fatiar o CPF
        fatia_1 = cpf[:3]
        fatia_2 = cpf[3:6]
        fatia_3 = cpf[6:9]
        fatia_4 = cpf[9:]
        
        cpf_formatado = f"{fatia_1}.{fatia_2}.{fatia_3}-{fatia_4}"
    
        return cpf_formatado
    
    except ValueError as e:
        return str(e)
    except Exception as e:
        return f"Erro inesperado: {e}"
    
    
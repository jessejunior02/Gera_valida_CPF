from utils.format_cpf import cpf_formatado
import random


def gerar_nove_digitos():
    return "".join(str(random.randint(0,9)) for _ in range(9))


def calcular_digito_verificador(digitos, sequencia_inicial):
    soma_digitos = 0
    for digito in digitos:
        soma_digitos += int(digito) * sequencia_inicial
        sequencia_inicial -= 1
    
    resto_divisao = soma_digitos % 11
    
    digito_verificador = 11 - resto_divisao
    return str(digito_verificador) if digito_verificador < 10 else "0"
    
    
def gerar_cpf(formatado=False):
    nove_digitos = gerar_nove_digitos()
    
    primeiro_digito = calcular_digito_verificador(nove_digitos, 10)
    segundo_digito = calcular_digito_verificador(nove_digitos+primeiro_digito, 11)
    
    cpf = f"{nove_digitos}{primeiro_digito}{segundo_digito}"
    
    return cpf_formatado(cpf) if formatado else cpf

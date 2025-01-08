from core import gerar_cpf, validar_cpf

def main():
    cpf = gerar_cpf(True) # True para ativar a formatação ###.###.###-##
    print(f"CPF gerado: {cpf}")
    
    print("-----------------------------")
    
    if validar_cpf(cpf):
        print(f"O CPF: {cpf} é válido")
    else:
        print(f"O CPF: {cpf} é inválido")
    
    
if __name__ == "__main__":
    main()
    
    # print(validar_cpf(53557052788)) # True
    # print(validar_cpf("53557052788")) # True
    # print(validar_cpf("535.570.527-88")) # True
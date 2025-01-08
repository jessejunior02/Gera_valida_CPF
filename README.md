# Gerador e Validador de CPF

Este projeto consiste em um gerador e validador de CPF implementado em Python. Ele gera CPFs válidos, formata-os corretamente e realiza a validação de CPFs existentes. A arquitetura do projeto está organizada de forma modular, separando a lógica principal, funções auxiliares e testes automatizados.

Observações: 
**Não foi utilizado GPT apenas DOCUMENTAÇÃO | Os testes serão implementados futuramente (De acordo com estudos)**

## Arquitetura do Projeto

```
gerador_cpf/
├── app.py                 # Ponto de entrada do aplicativo
├── core/                  # Lógica principal e regras de negócio
│   ├── __init__.py        # Torna a pasta um pacote Python
│   ├── cpf_validator.py   # Verifica se um CPF é válido
│   └── cpf_generator.py   # Gera CPFs válidos
├── utils/                 # Funções auxiliares e utilitárias
│   ├── __init__.py
│   └── format_cpf.py      # Formata um CPF no padrão ###.###.###-##
└── tests/                 # Testes automatizados
    └── test_cpf.py        # Testes para o gerador e validador de CPF
```

## Funcionalidades

- **Gerar CPF**: Gera um CPF válido com 11 dígitos, incluindo os dígitos verificadores.
- **Validar CPF**: Verifica se um CPF fornecido é válido, retornando `True` ou `False`.
- **Formatar CPF**: Formata o CPF no padrão `###.###.###-##`.

## Como Executar o Projeto

### 1. Clone o Repositório
```bash
git clone https://github.com/jessejunior02/Gera_valida_CPF.git
cd Gera_valida_CPF
```

### 2. Execute a Aplicação
```bash
python app.py
```

## Contribuição
Contribuições são bem-vindas! Se você deseja melhorar este projeto, sinta-se à vontade para enviar um Pull Request.

## Autor
- Github [Jesse Paiva Carvalho Junior](https://github.com/jessejunior02)
- LinkedIn [Jesse Paiva Carvalho Junior](https://www.linkedin.com/in/jessejuniordev/)


## LICENSE

[**MIT License**](https://opensource.org/license/mit)

***Copyright (c) 2025 Jesse Paiva C. Junior***

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.



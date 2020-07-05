#Desafio4 - Validador de CPF

print('Informe seu CPF (apenas números)')
print('=' * 32)
numero_cpf = str(input('Digite seu CPF: '))

if len(numero_cpf) == 11:
    print('CPF Válido')
else:
    print('CPF Inválido')



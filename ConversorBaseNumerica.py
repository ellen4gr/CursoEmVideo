"""Escreva imprograma que leia um número inteiro qualquer e peça para o usuário escolher qual será a base de
conversão 1 - binario, 2 - octal 3 - hexadecimal """
num = int(input('Digite um número inteiro: '))
print('''Escolha uma das bases para conversão:
[ 1 ] Converter para BINÁRIO
[ 2 ] Converter para OCTAL
[ 3 ] Converter para HEXADECIAMAL''')
opcao = int(input('Sua opção: '))

# escolhe a condição
if opcao == 1:
    print('{} convertido para BINÁRIO é igual a {}'.format(num, bin(num)[2:]))
elif opcao == 2:
    print('{} convertido para OCTAL é igual a {}'.format(num, oct(num)[2:]))
elif opcao == 3:
    print('{} convertido para HEXADECIAMAL é igual a {}'.format(
        num, hex(num)[2:]))
else:
    print('Opção inválida. Escolha de 1 a 3 ')

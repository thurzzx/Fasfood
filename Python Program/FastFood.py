
print('1- Hambúrguer - R$10,00')
print('2- Batata frita - R$5,00')
print('3- Rrefrigerante - R$4,00')
print('4- Sorvete - R$2,00')


opçao = int(input('1- Digite o n da opção desejada: '))
quantidade = int(input('digite a quantidade desejada: '))
nome = str(input('dogite o nome do cliente: '))

if opçao == 1:
    print('Hambuguer sendo preparado para ', nome)
    print('tempo de espera de 15 minutos')
    total = quantidade * 10 
    print('total: R$', total)
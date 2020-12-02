import time
total = 0
vfrete = 0
resposta = 'S'
while resposta == 'S':
    print('\t\t\t\t\t\033[1;32mRA Transpot´s\033[m\n')
    print('-=' * 27)
    print('\n\t\t\t\033[1;35mTABELA DE FRETE DE CAMINHÕES\033[m\n')
    print('-=' * 27)
    print('De km\t\t\tAté km\t\t\t\tCusto por km/Eixo')
    print(''' 
    1\t\t\t\t100\t\t\t\t\t\tR$ 2,14
    101\t\t\t\t200\t\t\t\t\t\tR$ 1,33
    201\t\t\t\t300\t\t\t\t\t\tR$ 1,17
    301\t\t\t\t400\t\t\t\t\t\tR$ 1,10
    401\t\t\t\t500\t\t\t\t\t\tR$ 1,06
    501\t\t\t\t600\t\t\t\t\t\tR$ 1,03
    601\t\t\t\t700\t\t\t\t\t\tR$ 1,02
    701\t\t\t\t800\t\t\t\t\t\tR$ 1,01
    801\t\t\t\t900\t\t\t\t\t\tR$ 1,00
    901\t\t\t\t1.000\t\t\t\t\tR$ 0,99
    1001\t\t\t1.100\t\t\t\t\tR$ 0,98
    1101\t\t\t1.200\t\t\t\t\tR$ 0,97
    ''')
    print('-=' * 27)
    nome = str(input('Digite aqui seu nome: '))
    while len(nome) == 0:
        print('\033[1;31mNOME NÃO FOI DIGITADO!\033[m', end='  ')
        nome = str(input('Digite seu nome por favor: '))
    km = float(input('Me informe quantos kilometro até o destinatário: (km) '))
    while km > 1200:
        print('\n\033[1;33mATENÇÃO!\033[m A distância não pode ultrapassar de 1.200km')
        km = float(input('Digite novamente: (km) '))
    while km < 0:
        print('\033[1;31m VALOR INCORRETO!\033[m')
        km = float(input('Digite o valor correto: '))
    if 0 <= km <= 100:
        vfrete = km * 2.14
        print(f'Sr(a). {nome},o valor do seu frete será de: R$ {vfrete:.2f}')
    elif 101 <= km <= 200:
        vfrete = km * 1.33
        print(f'Sr(a). {nome},o valor do seu frete será de: R$ {vfrete:.2f}')
    elif 201 <= km <= 300:
        vfrete = km * 1.17
        print(f'Sr(a). {nome},o valor do seu frete será de: R$ {vfrete:.2f}')
    elif 301 <= km <= 400:
        vfrete = km * 1.10
        print(f'Sr(a). {nome},o valor do seu frete será de: R$ {vfrete:.2f}')
    elif 401 <= km <= 500:
        vfrete = km * 1.06
        print(f'Sr(a). {nome},o valor do seu frete será de: R$ {vfrete:.2f}')
    elif 501 <= km <= 600:
        vfrete = km * 1.03
        print(f'Sr(a). {nome},o valor do seu frete será de: R$ {vfrete:.2f}')
    elif 601 <= km <= 700:
        vfrete = km * 1.02
        print(f'Sr(a). {nome},o valor do seu frete será de: R$ {vfrete:.2f}')
    elif 701 <= km <= 800:
        vfrete = km * 1.01
        print(f'Sr(a). {nome},o valor do seu frete será de: R$ {vfrete:.2f}')
    elif 801 <= km <= 900:
        vfrete = km * 1.00
        print(f'Sr(a). {nome},o valor do seu frete será de: R$ {vfrete:.2f}')
    elif 901 <= km <= 1000:
        vfrete = km * 0.99
        print(f'Sr(a). {nome},o valor do seu frete será de: R$ {vfrete:.2f}')
    elif 1001 <= km <= 1100:
        vfrete = km * 0.98
        print(f'Sr(a). {nome},o valor do seu frete será de: R$ {vfrete:.2f}')
    elif 1101 <= km <= 1200:
        vfrete = km * 0.97
        print(f'Sr(a). {nome},o valor do seu frete será de: R$ {vfrete:.2f}')
    elif resposta == 'N':
        break
    print('-=' * 27)
    print('\t\t\t\033[1;35mTABELA DE PREÇO ENCOMENDA\033[m')
    print('-=' * 27)
    print('''
    Até 100 kg\t\t\t\tR$ 85,00
    Até 200 kg\t\t\t\tR$ 130,00
    Até 300 kg\t\t\t\tR$ 250,00
    Até 400 kg\t\t\t\tR$ 315,00
    Até 500 kg\t\t\t\tR$ 460,00
    ''')
    print('-=' * 27)
    kg = float(input('Informe o peso da sua mercadoria: (kg) '))
    while kg > 500:
        print('\033[1;33mATENÇÃO!\033[m Peso Maximo suportado é de 500kg.', end='')
        kg = float(input('Por favor digite o peso novamente: (kg) '))
    while kg < 0:
        print('\033[1;31m VALOR INCORRETO!\033[m')
        kg = float(input('Digite um valor correto: '))
    print('\nOk,um momento que iremos calcular')
    time.sleep(1.5)
    print('.', end='')
    time.sleep(1.5)
    print('.', end='')
    time.sleep(1.5)
    print('.', end='')
    time.sleep(1.5)
    print('.', end='')
    time.sleep(1.5)
    print('.', end='')
    time.sleep(1.5)
    print('.', end='')
    time.sleep(1.5)
    print('.', end='')
    time.sleep(1.5)
    print('.', end=' ')
    print('\033[1;32mPRONTO!\033[m\n')
    time.sleep(2)
    if 0 >= kg <= 100:
        total = 85 + vfrete
        print(f'Com o frete de R${vfrete:.2f} mais a encomenda de {kg}kg, valor final será R$ {total:.2f}')
    elif 101 <= kg <= 200:
        total = 130 + vfrete
        print(f'Com o frete de R${vfrete:.2f} mais a encomenda de {kg}kg, valor final será R$ {total:.2f}')
    elif 201 <= kg <= 300:
        total = 250 + vfrete
        print(f'Com o frete de R${vfrete:.2f} mais a encomenda de {kg}kg, valor final será R$ {total:.2f}')
    elif 301 <= kg <= 400:
        total = 315 + vfrete
        print(f'Com o frete de R${vfrete:.2f} mais a encomenda de {kg}kg, valor final será R$ {total:.2f}')
    elif 401 <= kg <= 500:
        total = 460 + vfrete
        print(f'Com o frete de R${vfrete:.2f} mais a encomenda de {kg}kg, valor final será R$ {total:.2f}')
    resposta = str(input('Quer continuar? [S / N] ')).strip().upper()[0]
    for i in range(500):
        print()
    while resposta not in 'SN':
        print('\033[1;31mLETRA INCORRETA!\033[m', end='')
        resposta = str(input('Digite novamente, Quer continuar? [S / N] ')).strip().upper()[0]
        if resposta == 'N':
            print('PROGRAMA FINALIZADO')
            break
    for i in range(100):
        print()



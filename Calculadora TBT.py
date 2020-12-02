print('\t\033[1;32m Calculadora de TBM\033[m')
resposta = 'S'
while resposta == 'S':
    nome = str(input('\nMe informe seu nome: '))
    peso = float(input('Qual é o seu peso (kg): '))
    idade = int(input('Qual é a sua idade: '))
    altura = float(input('Qual a sua altura (cm): '))
    sexo = str(input('Qual seu sexo \033[1;34mM\033[m / \033[1;35mF\033[m : ')).title().strip()
    if sexo == 'M':
        tbm = 66 + (13.7 * peso) + (5 * altura) - (6.8 * idade)
        print(f'{nome},sua TAXA METABÓLICA BASAL é  \033[1;31m{tbm:.2f}\033[m')
    else:
        tbm = 65 + (9.6 * peso) + (1.8 * altura) - (4.7 * idade)
        print(f'{nome},sua TAXA METABÓLICA BASAL é  \033[1;31m{tbm:.2f}\033[m')
    print('-=' * 50)
    print('\033[33mNIVEL DE ATIVIDADE                                      EQUAÇÃO DO GASTO ENERGÉTICO\033[m ')
    print('-=' * 50)
    print('''
    [1]Sedentário pouco um nenhum exercicio              |  Gasto energético   Total =  TBM  X 1,2     
    [2]Exercicio leve (1-3 dias por semana)              |  Gasto energético   Total =  TBM  X 1,375            
    [3]Exercicio moderado (3-5 dias por semana)          |  Gasto energético   Total =  TBM  X 1,55
    [4]Exercicio pesado (6-7 dias por semana)            |  Gasto energético   Total =  TBM  X 1,725
    [5]Exercicio muito pesado (duas vezes por dia,       |  Gasto energético   Total =  TBM  X 1,9
    extras treinos pesados)                              |
    ''')
    print('-=' * 50)
    item = int(input('Qual opção deseja? '))
    if item == 1:   
        get = tbm * 1.2
        print(f'Seu GASTO ENERGÉTICO TOTAL é \033[1;31m{get:.2f}\033[m')
    if item == 2:
        get = tbm * 1.375
        print(f'Seu GASTO ENERGÉTICO TOTAL é \033[1;31m{get:.2f}\033[m')
    if item == 3:
        get = tbm * 1.55
        print(f'Seu GASTO ENERGÉTICO TOTAL é \033[1;31m{get:.2f}\033[m')
    if item == 4:
        get = tbm * 1.725
        print(f'Seu GASTO ENERGÉICO TOTAL é \033[1;31m{get:.2f}\033[m')
    if item == 5:
        get = tbm * 1.9
        print(f'Seu GASTO ENERGÉTICO TOTAL é \033[1;31m{get:.2f}\033[m')
    resposta = str(input('\nQuer continuar [S/N] ?')).strip().upper()[0]
    while resposta not in 'SN':
        resposta = str(input('\033[1;31mLETRA INCORRETA\033[m,digite novamente [S / N] para continuar: ')).strip().upper()[0]
        if resposta == 'N':
            break

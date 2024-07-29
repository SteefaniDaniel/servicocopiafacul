
#funçao para escolher o serviço desejadd

def escolha_servico():
    valor_servico = 0
    while True:
        opcao = ['DIG', 'ICO', 'IBO', 'FOT']
        servico = str(input('Escolha o servico desejado: DIG-Digitalização/ICO-Impressão Colorida/IBO-Impressão preto e branco/FOT-Fotocópia:'))
        valor_servico = 0
        if servico in opcao:
            if servico == 'DIG':
                valor_servico += 1.10
                return valor_servico
            elif servico == 'ICO':
                valor_servico += 1.00
                return valor_servico
            elif servico == 'IBO':
                valor_servico += 0.40
                return valor_servico
            elif servico == 'FOT':
                valor_servico += 0.20
                return valor_servico
        else:
            print('Serviço Inválido. Escolha os serviços:DIG,ICO,IBO ou FOT!')
            continue

#função para escolher o número de páginas
def num_paginas():
    desconto = 0
    while True:
        try:
            numerode_paginas = int(input('Digite o número de páginas que deseja:'))
            if numerode_paginas <= 20:
                print('Você escolheu {} páginas.Seu desconto é de 0%'.format(numerode_paginas))
                return numerode_paginas, 0
            elif (numerode_paginas >= 20) and (numerode_paginas < 200):
                print('Você escolheu {} páginas.Seu desconto é de 15%'.format(numerode_paginas))
                return numerode_paginas, 0.15
            elif numerode_paginas >= 200 and numerode_paginas < 2000:
                print('Você escolheu {} páginas.Seu desconto é de 20%'.format(numerode_paginas))
                return numerode_paginas, 0.20
            elif numerode_paginas >= 2000 and numerode_paginas < 20000:
                print('Você escolheu {} páginas.Seu desconto é de 25%'.format(numerode_paginas))
                return numerode_paginas, 0.25
            else:
                print('Ops.Não aceitamos tantas páginas de vez,escolha novamente!')
                continue
        except ValueError:
            print('Opção inválida.Por favor,digite um número válido inteiro!')



#funçao para escolher o serviço extra
def servico_extra():
    adicional = int(input('Deseja adicionar algum serviço extra? 1-Encadernação Simples/2-Encadernação Capa dura/0-Não quero adicional:'))
    extra = 0
    if adicional in [1, 2, 0]:
        if adicional == 1:
            extra += 15.00
            return extra, adicional
        elif adicional == 2:
            extra += 40.00
            return extra, adicional
    else:
        print('Serviço inválido. Tente novamente!')

#programa principal
print('Olá,seja bem vindo(a) ao sistema de Copiadora da Stéfani!')
servico = escolha_servico()
numerode_paginas,desconto = num_paginas()
extra,adicional = servico_extra()
total = (servico * numerode_paginas) - ((servico * numerode_paginas)*desconto) + extra
print('O valor total é de: R${}.'.format(total))














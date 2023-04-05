#Os dados colados aqui foram copiados dos exercicios anteriores
from datetime import date
hoje = date.today()
dia = hoje.day
mes = hoje.month
ano = hoje.year

nomes = []
cpfs = []
nascimentos = []
dias_mes = [31,28,31,30,31,30,31,31,30,31,30,31] #lista com os dias de cada mês para calculos
mes_31 = [1,3,5,7,8,10,12]
mes_30 = [4,6,9,11]
alfabeto = 'AÁÀÃÂBCÇDEÉÊFGHIÍJKLMNOÓÔÕPQRSTUÚÜVWXYZaáàãâbcçdeéêfghiíjklmnoóôõpqrstuúüvwxyz'

#estrutura de repetição para gerar o menu
while True:
  sit_id = True #usado para verificar se o id é um número inteiro
  sit_nome = True #usado para verificar se o nome não tem numero
  sit_cpf = True #usado para verificar o cpf
  sit_data = True #usado para verificar se a data está no formato correto
  print('1. Inserir novo cadastro\n2. Alterar CPF\n3. Trocar sobrenomes\n4. Remover cadastro\n5. Listar todos os cadastros\n6. Encerrar')
  opcoes = input('Insira a opção desejada (Número inteiro): ')
  if opcoes == '1':
    print('Os campos Nome, CPF e Nascimento são obrigatorios')
    id = input('Insira o ID: ')
    for i in range(len(id)):
      if id[i] not in '0123456789': #percorrendo os itens do id para verificar se é inteiro
        print('O ID deve ser um número inteiro!')
        sit_id = False
        break
    if not sit_id:
      continue
    if int(id) > (len(nomes)+1) or int(id) < 1:#verificando validade do id
      print('O ID informado é inválido')
      continue
    nome = input('Insira o Nome e Sobrenome (Formato: Nome Sobrenome): ')
    #verificando se não a o espaço necessario
    if nome.count(' ') != 1:
      print('Nome inserido é inválido!')
      continue
    #verificando o tamanho adequado
    if len(nome) < 6:
      print('Nome inserido é inválido!')
      continue
    id_meio = nome.find(' ')
    nome_trat = nome[:id_meio].capitalize()
    sobre_trat = nome[id_meio+1:].capitalize()
    if len(nome_trat) < 3:
      print('Nome inserido é inválido!')
      continue
    if len(sobre_trat) < 3:
      print('Nome inserido é inválido!')
      continue
    for i in range(len(nome_trat)): #percorrendo os itens do id para verificar se é inteiro
      if nome_trat[i] not in alfabeto:
        print('Nome inserido é inválido!')
        sit_nome = False
        break
    if not sit_nome:
      continue
    for i in range(len(sobre_trat)): #percorrendo os itens do id para verificar se é inteiro
      if sobre_trat[i] not in alfabeto:
        print('Nome inserido é inválido!')
        sit_nome = False
        break
    if not sit_nome:
      continue
    nome = f'{nome_trat} {sobre_trat}'
    cpf = input('Insira o CPF (Sem ponto e sem hífen): ')
    if len(cpf) != 11:#verificando se há 11 digitos
      print('CPF inserido é inválido pois não contém 11 digitos!')
      continue
    for i in range(len(cpf)):
      if cpf[i] not in '0123456789':#verificando se todos são numeros
        print('CPF inserido é inválido pois contém letras ou caracteres especiais!')
        sit_cpf = False
        break
    if not sit_cpf:
      continue
    if cpf[8] in '678':#verificando a região
      print('CPF inserido é inválido, pois foi emitido na Região Sudeste!')
      continue
    dig_ver_1 = int(cpf[0]) * 10 + int(cpf[1]) * 9 + int(cpf[2]) * 8 + int(cpf[3]) * 7 + int(cpf[4]) * 6 + int(cpf[5]) * 5 + int(cpf[6]) * 4 + int(cpf[7]) * 3 + int(cpf[8]) * 2
    dig_ver_1 %= 11
    if dig_ver_1 == 0 or dig_ver_1 == 1:
      dig_ver_1 = 0
    else:
      dig_ver_1 = 11 - dig_ver_1
    
    dig_ver_2 = int(cpf[1]) * 10 + int(cpf[2]) * 9 + int(cpf[3]) * 8 + int(cpf[4]) * 7 + int(cpf[5]) * 6 + int(cpf[6]) * 5 + int(cpf[7]) * 4 + int(cpf[8]) * 3 + int(cpf[9]) * 2
    dig_ver_2 %= 11
    if dig_ver_2 == 0 or dig_ver_2 == 1:
      dig_ver_2 = 0
    else:
      dig_ver_2 = 11 - dig_ver_2
    if int(cpf[9]) != dig_ver_1 or int(cpf[10]) != dig_ver_2:
      print('CPF inserido é inválido!')
      continue
    nascimento = input('Insira a data de nascimento (Formato dd/mm/aaaa): ')
    if len(nascimento) != 10:
      print('A Data está em um formato inválido!')
      continue
    #verificando se as barras estão nos locais corretos
    if (nascimento[2] == nascimento[5] == '/'):
      for i in range(len(nascimento)):
        if i == 2 or i == 5:
          continue
        if nascimento[i] not in '0123456789':#verificando se todos são numeros
          print('A Data está em um formato inválido!')
          sit_data = False
          break
    else:
      print('A Data está em um formato inválido!')
      continue
    if not sit_data:
      continue
    #verificar se é uma data possivel e separando o dia, mês e ano
    dia_nasc = int(nascimento[:2])
    mes_nasc = int(nascimento[3:5])
    ano_nasc = int(nascimento[6:])
    #verificando se é maior que o ano atual
    if ano_nasc > ano:
      print('A Data informada ainda não chegou!')
      continue
    #verificando se é igual ao ano atual
    elif ano_nasc == ano:
      #verificando se é maior que o mes atual
      if mes_nasc > mes:
        print('A Data informada ainda não chegou!')
        continue
      #verificando se é igual ao mes atual
      elif mes_nasc == mes:
        #verificando se é maior que o dia atual
        if dia_nasc > dia:
          print('A Data informada ainda não chegou!')
          continue
    #verificando se os dias e meses são valido(existentes)
    if dia_nasc < 1:
      print('A Data informada não existe!')
      continue
    if mes_nasc < 1 or mes_nasc > 12:
      print('A Data informada não existe!')
      continue
    if mes_nasc in mes_30:
      if dia_nasc > 30:
        print('A Data informada não existe!')
        continue
    elif mes_nasc in mes_31:
      if dia_nasc > 31:
        print('A Data informada não existe!')
        continue
    else:
      if (ano_nasc % 4 == 0 and ano_nasc % 100 != 0) or ano_nasc % 400 == 0:
        if dia_nasc > 29:
          print('A Data informada não existe!')
          continue
      elif dia_nasc > 28:
        print('A Data informada não existe!')
        continue
  #Estrutura condicional para verificar se os dados obrigatorios forma informados
    if nome != '' and cpf != '' and nascimento != '':
    #Estrutura condicional para verificar se o ID foi informado
      if id == '':#verificando validade do id
        nomes.append(nome)
        cpfs.append(cpf)
        nascimentos.append(nascimento)
      else: 
        id = int(id) - 1
        nomes.insert(id, nome)
        cpfs.insert(id, cpf)
        nascimentos.insert(id, nascimento)
      print('Cadastro inserido com sucesso!')
    # else:
    #   print('Os campos Nome, CPF e Nascimento são obrigatorios!')
    #   print('O cadastro não foi realizado!')
    continue
  elif opcoes == '2':
    #informação de qual id deve ser alterado
    id = input('Insira o id que deseja alterar: ')
    for i in range(len(id)):
      if id[i] not in '0123456789':
        print('O ID deve ser um número inteiro!')
        sit_id = False
        break
    if not sit_id:
      continue
    id = int(id)
    if id > (len(cpfs)) or id < 1:
      print('O ID informado é inválido')
      continue
    
    #Pegando o dado que será inserido na informação do cpf
    cpf = input(f'Insira o novo CPF para o ID {id}: ')
    if len(cpf) != 11:#verificando se há 11 digitos
      print('CPF inserido é inválido pois não contém 11 digitos!')
      continue
    for i in range(len(cpf)):
      if cpf[i] not in '0123456789':#verificando se todos são numeros
        print('CPF inserido é inválido pois contém letras ou caracteres especiais!')
        sit_cpf = False
        break
    if not sit_cpf:
      continue
    if cpf[8] in '678':#verificando a região
      print('CPF inserido é inválido, pois foi emitido na Região Sudeste!')
      continue
    #calculando os digitos verificadores do cpf
    dig_ver_1 = int(cpf[0]) * 10 + int(cpf[1]) * 9 + int(cpf[2]) * 8 + int(cpf[3]) * 7 + int(cpf[4]) * 6 + int(cpf[5]) * 5 + int(cpf[6]) * 4 + int(cpf[7]) * 3 + int(cpf[8]) * 2
    dig_ver_1 %= 11
    if dig_ver_1 == 0 or dig_ver_1 == 1:
      dig_ver_1 = 0
    else:
      dig_ver_1 = 11 - dig_ver_1
    dig_ver_2 = int(cpf[1]) * 10 + int(cpf[2]) * 9 + int(cpf[3]) * 8 + int(cpf[4]) * 7 + int(cpf[5]) * 6 + int(cpf[6]) * 5 + int(cpf[7]) * 4 + int(cpf[8]) * 3 + int(cpf[9]) * 2
    dig_ver_2 %= 11
    #verificando se os digitos verificadores confirmam
    if dig_ver_2 == 0 or dig_ver_2 == 1:
      dig_ver_2 = 0
    else:
      dig_ver_2 = 11 - dig_ver_2
    if int(cpf[9]) != dig_ver_1 or int(cpf[10]) != dig_ver_2:
      print('CPF inserido é inválido!')
      continue
    #alterando o cpf referente ao id
    cpfs[id-1] = cpf
    continue
  elif opcoes == '3':
    id = input('Insira o id que deseja trocar o sobrenome: ')
    for i in range(len(id)):
      if id[i] not in '0123456789':
        print('O ID deve ser um número inteiro!')
        sit_id = False
        break
    if not sit_id:
      continue
    id = int(id)
    if id > (len(nomes)) or id < 1:
      print('O ID informado é inválido, pois não existe!')
      continue
    #separando e tratando o nome e sobrenome para troca
    pri_id = id - 1
    pri_id_meio = nomes[pri_id].find(' ')
    nome_pri = nomes[pri_id][:pri_id_meio]
    sobre_pri = nomes[pri_id][pri_id_meio+1:]
    id = input(f'Insira o id que será trocado o sobrenome com ID {pri_id+1}: ')
    for i in range(len(id)):
      if id[i] not in '0123456789':
        print('O ID deve ser um número inteiro!')
        sit_id = False
        break
    if not sit_id:
      continue
    id = int(id)
    if id > (len(nomes)) or id < 1:
      print('O ID informado é inválido, pois não existe!')
      continue
    #separando e tratando o nome e sobrenome para troca
    seg_id = id - 1
    seg_id_meio = nomes[seg_id].find(' ')
    nome_seg = nomes[seg_id][:seg_id_meio]
    sobre_seg = nomes[seg_id][seg_id_meio+1:]
    nomes[pri_id] = f'{nome_pri} {sobre_seg}'
    nomes[seg_id] = f'{nome_seg} {sobre_pri}'
    continue
  elif opcoes == '4':
    #informação de qual id deve ser removido
    id = input('Insira o id que deseja remover: ')
    for i in range(len(id)):
      if id[i] not in '0123456789':
        print('O ID deve ser um número inteiro!')
        sit_id = False
        break
    if not sit_id:
      continue
    id = int(id)
    if id > (len(nomes)) or id < 1:
      print('O ID informado é inválido, pois não existe!')
      continue
    #Removendo os dados do id informado em todas as listas
    nomes.pop(id-1)
    cpfs.pop(id-1)
    nascimentos.pop(id-1)
    continue
  elif opcoes == '5':
    idades_dias = []
    for i in range(len(nascimentos)):
      #separando os dias, mês e ano
      dia_nasc = int(nascimentos[i][:2])
      mes_nasc = int(nascimentos[i][3:5])
      ano_nasc = int(nascimentos[i][6:])
      cont = ano_nasc
      quant_anos_bis = 0
  #verificando se o ano de nascimento é bissexto
      if (ano_nasc % 4 == 0 and ano_nasc % 100 != 0) or ano_nasc % 400 == 0:
        if mes_nasc < 2:
          quant_anos_bis += 1
          cont += 1
  #vereficando quantos anos são bissextos
      while cont < ano:
        if (cont % 4 == 0 and cont % 100 != 0) or cont % 400 == 0:
           quant_anos_bis += 1
        cont += 1
      dias_fim_ano = 0
      i = mes_nasc
  #verificando quantos dias tem do nascimento até o fim daquele ano
      while i < len(dias_mes):
        dias_fim_mes = dias_mes[mes_nasc-1] - dia_nasc
        dias_fim_ano += dias_mes[i]
        i += 1
      dias_inicio_atual_ano = 0
      dias_inicio_fim = 0
      j = 0
      #verificando quantos dias já tiveram no ano vigente
      while j < mes:
        dias_inicio_fim = dia
        dias_inicio_atual_ano += dias_mes[j-1]
        j += 1
        #somando para verificar o total de dias desde o nascimento
      idade_dias = ((ano - (ano_nasc+1)) * 365) + dias_fim_mes + dias_fim_ano + dias_inicio_fim + dias_inicio_atual_ano - dias_mes[mes-1] + quant_anos_bis
  #inserindo os dias na lista
      idades_dias.append(idade_dias)
    #Estrutura condicional para verificar se há algun cadastro
    if len(nomes) > 0:
    #Estrutura de repetição para a exibição das informações de cadastro
      for i in range(len(nomes)):
        print(f'ID: {i+1} - Nome: {nomes[i]} - CPF: {cpfs[i]} - Data de Nascimento: {nascimentos[i]} - Idade em dias: {idades_dias[i]}')
    else:
      print('Não há nenhum cadastro armazenado!')
    continue
  elif opcoes == '6':
    print('Programa encerrado!')
    break
  else:
    print('Nenhuma opção válida foi selecionada, tente novamente!')
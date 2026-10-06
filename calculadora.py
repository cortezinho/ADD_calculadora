# Pergunta nome do usuário
nome_usuario = input('Olá, qual o seu nome? ')
print(f'Seja bem-vindo {nome_usuario}!')
print('Vamos fazer umas operações matemáticas!')

# Dicionario de operações
operacoes = {
    '1': 'Adição',
    '2': 'Subtração',
    '3': 'Multiplicação',
    '4': 'Divisão',
    '5': 'Potenciação'
    }

# Variável de controle do loop principal da aplicação
flag = True
while flag:

  # Recebendo a entrada e fazendo validações
  # Validação para o primeio numero
  while True:
    num1 = input('Digite um número:')
    try:
        num1 = int(num1)
        break
    except ValueError:
        print('Digite apenas numeros inteiros!')

  # Validação para o segundo numero
  while True:
    num2 = input('Digite outro número: ')
    try:
        num2 = int(num2)
        break
    except ValueError:
        print('Digite apenas numeros inteiros!')


  # perguntando ao usuário qual operação el quer
  operacao_escolhida = input('Lista de operações \n1 - Soma \n2 - Subtração \n3 - Multiplicação \n4 - Divisão \n5 - Potenciação \nEscolha qual operação você quer realizar:')

  # Valida se o usuário escolheu uma operação da lista
  while True:
      if operacao_escolhida not in operacoes:
          print('Operação inválida!')
          operacao_escolhida = input('Escolha uma operação da lista:')
      else:
          print(f'A operação escolhida foi: {operacoes[operacao_escolhida]}')
          break


  # Calculos das operações

  # Adição
  if operacao_escolhida == '1':
      resultado = num1 + num2
      print(f'O resultado é: {resultado}')

  # Subtração
  elif operacao_escolhida == '2':
      resultado = num1 - num2
      print(f'O resultado é: {resultado}')

  # Multiplicação
  elif operacao_escolhida == '3':
      resultado = num1 * num2
      print(f'O resultado é: {resultado}')

  # Divisão - validando se o segundo numero é 0
  elif operacao_escolhida == '4':
      if num2 == 0:
          print('Não é possivel dividir por zero')
      else:
          resultado = int(num1 / num2)  # convertendo resultado em inteiro
          print(f'O resultado é: {resultado}')

  # Potenciação
  elif operacao_escolhida == '5':
      resultado = num1 ** num2
      print(f'O resultado é: {resultado}')


  # Pergunta se o usuário quer fazer outra operação
  while True:
    continuar = input('Gostaria de realizar outra operação? (s/n): ').lower().strip()  # Convertendo para minúsculo e removendo espaços em branco
    if continuar in ('s' , 'n'):
        if continuar == 's':
          print('Ok, continuando!')
          break
        elif continuar == 'n':
          print('Tchau, Obrigado!')
          flag = False
          break
    else:
        print('Resposta inválida')

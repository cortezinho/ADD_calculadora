# ADD_calculadora

Repositório destinado à atividade do curso de Analista de Dados.

## Sobre o Projeto

O programa é uma calculadora interativa para terminal que realiza operações básicas entre dois números.

## Funcionalidades
- Solicita o nome do usuário.
- Recebe dois números com validação de entrada.
- Permite escolher entre 5 operações:
  * 1 - Soma
  * 2 - Subtração
  * 3 - Multiplicação
  * 4 - Divisão
  * 5 - Potenciação
- Possui validação para menu de opções e divisão por zero.
- Permite realizar novos cálculos em loop ou encerrar a execução ("s" para continuar, "n" para sair).

## Requisitos
- A maquina tem que ter como sistema operacional o Linux com a distribuição Ubuntu.
- Também pode funcionar com WSL.

## Como Executar

1. Clone ou baixe os arquivos "calculadora.py" e "calculadora.sh" para a sua máquina.
2. Abra o arquivo "calculadora.sh" e ajuste o caminho do script "calculadora.py" para o diretório do seu usuário no Ubuntu/WSL:
```
/seu_usuario/caminho/para/calculadora.py
```
3. De permissão de execução para o arquivo calculadora.sh com o comando:
```
chmod u+rwx calcuadora.sh
```
4. Execute o arquivo calculadora.sh com o comando:
```
./calculadora.sh
```

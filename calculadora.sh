#!/bin/bash

echo "Iniciando o Script"

echo "Atualizando pacotes"

# Atualiza os pacotes
sudo apt update

echo "Instalando/Atualizando Python"

# Instala/Atualiza o Python versão 3
sudo apt install -y python3

echo "Abrindo a calculadora"

# Executa a calculadora
python3 /home/cortez/atividadeLinux/calculadora.py

#!/bin/bash

# Criar 5 arquivos
for i in 1 2 3 4 5;
do
  echo $i > "./test/arquivo_$i.txt"  # Escreve o número no arquivo
  echo "Arquivo arquivo_$i.txt criado com conteúdo: $i"
done

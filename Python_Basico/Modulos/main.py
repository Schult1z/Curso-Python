# Puxando a funcao - MODULARIZACAO
import funcoes #modulo - para puxar de uma pasta (from (pasta) import (nome do arq))
funcoes.saudacao("Gabriel")

from funcoes import saudacao
saudacao("Amaral")

from funcoes import somar
print(somar(6, 7))

from funcoes import subtrair
print(subtrair(10,6))
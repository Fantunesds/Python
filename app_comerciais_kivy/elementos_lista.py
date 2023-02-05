"""
INCLUIR ALTERAR E EXCLUIR ELEMENTOS DE UMA LISTA

"""

lista = ['bbb','ccc','ddd']

lista.append('aaa')# acresenta um item a lista 
lista.insert(0,'aaaa') # acresenta um item na lista em determinada posição
#lista.clear() # limpa os dados da lista
#lista.pop() #exclui o ultimo elemento da lista por padrão ou indique o elemento dentro dos parenteses
del(lista[2:4]) # exclui elementos da lista pode ser digitado em qualquer lugar do codigo.


print(lista)
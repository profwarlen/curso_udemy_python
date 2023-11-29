nome='warlen'
idade=48
'''
No código abaixo, o 'f' antes das aspas é um prefixo especial chamado "f-string" (format string) introduzido em Python 3.6. 

As f-strings são uma maneira conveniente de formatar strings de forma mais legível e concisa. Elas permitem a interpolação de variáveis diretamente dentro da string, colocando-as entre chaves `{}`. 

Neste exemplo, o valor das variáveis `nome` e `idade` será inserido na string final quando ela for impressa. Isso facilita a concatenação de variáveis ​​e valores em uma string sem a necessidade de usar operadores de formatação ou concatenação.

Essa sintaxe é conhecida como "f-string" porque a letra 'f' antes das aspas indica que a string deve ser formatada dessa maneira especial.

Em resumo, o uso do 'f' antes das aspas permite a interpolação de variáveis dentro das chaves `{}` em uma string, tornando a formatação de strings mais simples e legível.

'''
print(f'meu nome é {nome} e tenho {idade}')
print('meu nome é ' + nome + ' e tenho ' + str(idade))
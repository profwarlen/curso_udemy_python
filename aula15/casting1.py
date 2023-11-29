'''
Neste exemplo mostrarei como printar variável string com inteiro
no primeiro exemplo dará erro pois não fiz o casting
e no segundo farei o casting
'''

#primeiro exemplo que dará erro pois idade é int
nome='warlen'
idade=48

print('meu nome é '+ nome + ' e tenho ' + idade + ' anos')

'''
Reportou o erro abaixo pois idade é um número inteiro e o python não coseguiu converer para string, já que o argumento do print só aceita texto :
TypeError: can only concatenate str (not "int") to str
PS C:\Users\field163\Desktop\PYTHON\CURSO_UDEMY_PYTHON\curso_udemy_python>
'''


#no arquivo casting2.py farei a correção
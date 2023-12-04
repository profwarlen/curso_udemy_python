# Default: Aquele que você define o valor do parâmentro
# Non-default: Aquele que você não define o valor no parâmetro

def boas_vindas(nome,quantidade=6):
    #quantidade=default - nome=non-default
    print(f'Olá {nome}')
    print(f'Temos {quantidade} laptops no estoque')


boas_vindas('warlen')#como não coloquei a quantidade irá inserir 6 que é default
boas_vindas('warlen',4)#agora sobrescrevi o valor padrão


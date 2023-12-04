#Publicar um produto com comissão de 10% se for acima de R$ 20,00


# valor=int(input('Digite o valor do seu produto R$: '))

# while valor>20:
#     valor=(valor*0.10)+valor
#     print(f'O valor do seu produt final será de R$ {valor}')
#     break


#Outra forma de calcular 10%

valor=int(input('Digite o valor do seu produto R$: '))


while valor>20:
    valor=round(valor*1.1,2)
    print(type(valor))
    print(f'O valor do seu produt final será de R$ {valor}')
    break


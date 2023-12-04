#mesmo eu dubplicando o nome das variáveis não da erro pois estão em funções diferentes
def somar_dois_numros():
    numero1=10
    numero2=5
    resultado=numero1+numero2
    print(resultado)

def somar_dois_numros1():
    numero1=1
    numero2=5
    resultado=numero1+numero2
    print(resultado)

somar_dois_numros()
somar_dois_numros1()

#Dará o erro abaixo, pois a variável resultado não é global e sim está dentro de uma função e não temos acesso a ela:
# NameError: name 'resultado' is not defined
# print(resultado)
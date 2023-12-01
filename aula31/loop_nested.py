# loop nested - loop dentro de outro loop
# outer loop
#inner loop

for numero1 in range(5):
    print(numero1)
    print('-------')
    for numero2 in range(5):
        print(numero2)

print('\n======================================')

for nummero3 in range(1,6):
    print('produto'+str(nummero3))
    for numero4 in range(5):
        print(nummero3,numero4)
        print('----------')
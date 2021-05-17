def chequeoPrimo(numero):
    for rango in range(2,numero):
        if numero%rango==0:
            return False
    return True

numeroNatural = int(input('Ingrese Numero Natural: '))
columna = 0

print(f'Primos entre 1 y {numeroNatural}:\n')
for i in range(2, numeroNatural):
    resultado = chequeoPrimo(i)

    if resultado:
        columna+=1

        print(i, end='\t')
        if columna%10==0:
            print('\n')


print(f'\n\nPrimeros {numeroNatural} Primos:\n')
primosContador = 0
test=2
columna=0

while primosContador < (numeroNatural):

    resultado = chequeoPrimo(test)
    if resultado:
        columna+=1
        primosContador+=1

        print(test, end='\t')
        if columna%10==0:
            print('\n')

    # Numeros Input de Funcion
    test+=1
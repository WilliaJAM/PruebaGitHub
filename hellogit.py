print('Segundo fichero')
print('Modifiación')

input_user = input('Ingresa tu nombre')

print(f'Hola, {input_user}')

#Un XD

#TODO: En el ultimo if no esta valdando correctamente.
def caffeine_buzz(n):

    phrase = 'mocha_missing!'

    if n % 3 == 0 and n % 4 == 0:
        phrase = 'Coffee'
    elif n % 3 == 0:
        phrase = 'Java'

    if (n % 3 == 0 or n % 4 == 0) and n % 2 == 0:
        phrase += 'Script'

    return phrase


print(caffeine_buzz(4))
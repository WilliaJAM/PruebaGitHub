print('Segundo fichero')
print('Modifiación')

# input_user = input('Ingresa tu nombre')

# print(f'Hola, {input_user}')

#Un XD

#TODO: En el ultimo if no esta valdando correctamente.
def caffeine_buzz(n):

    phrase = 'mocha_missing!'
    validate = False

    if n % 3 == 0 and n % 4 == 0:
        phrase = 'Coffee'
        validate = not validate
    elif n % 3 == 0:
        phrase = 'Java'
        validate = not validate

    if validate and n % 2 == 0:
        phrase += 'Script'

    return phrase


print(caffeine_buzz(4))
print('Segundo fichero')
print('Modifiación')

input_user = input('Ingresa tu nombre')

print(f'Hola, {input_user}')

#Un XD

#Terminar
def caffeine_buzz(n):

    phrase = ''

    if n % 3 == 0 and n % 4 == 0 and n % 2 == 0:
        return 'mocha_missing!'

    if n % 3 == 0 and n % 4 == 0:
        phrase = 'Coffee'
    
    if n % 3 == 0:
        phrase = 'Java'

    return phrase + 'Script'

#Comentario desde el pasado
def xd():
    return 'Hola mundo'


num_user = int(input('Ingrese su numero'))


if (num_user % 3 == 0 and num_user % 7 == 0) :
    print('FizzBuzz')
else:
    if(num_user % 3 == 0):
        print('Fizz')
    elif(num_user % 7 == 0):
        print('Buzz')
    else:
        print('El Giro')

print('Muy bien.., hagamos esto una ultima vez.')
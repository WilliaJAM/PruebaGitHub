def xd():
    return 'Hola mundo'


num_user = int(input('Ingrese su numero'))


if (num_user % 3 == 0 and num_user % 7 == 0) :
    print('FizzBuzz')
else:
    if(num_user % 3 == 0):
        print('Fizz')
    
    if(num_user % 7 == 0):
        print('Buzz')
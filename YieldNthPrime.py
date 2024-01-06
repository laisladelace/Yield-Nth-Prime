def is_prime(n):
    if n ==1: 
        return False 
    for i in range (2,n):
        if n%i==0:
            return False
    else: return True 

def yield_nth_prime():
    n = int (input("Enter n:"))
    _zero= 0 
    _two = 2 
    while _zero < n: 
        if is_prime(_two):
            _zero +=1
        if _zero ==n:
            return _two
        _two+=1


print (yield_nth_prime(7))




#Just in case you didn't get the invite for the other repository: 

import time 
start = time.time()


def find_a_list_of_prime_numbers():

    print ('Choose a range (from x through y)')
    x_value = int(input('Enter x(greater than 1):'))
    y_value = int(input('Enter y:'))

    list_prime_num = []
    for number in range(x_value, y_value +1):
        for n in range (2, number):
            if number %n==0:
                break 
            else: 
                list_prime_num.append(number)
    print()
    print(f'Prime numbers between {x_value} and {y_value} are:')
    for prime in list_prime_num:
        print(f'{prime}', end = '')
    print()

find_a_list_of_prime_numbers()

end = time.time()
print (f"The total run time for the program was:")
print(round(end-start,2)),"seconds")

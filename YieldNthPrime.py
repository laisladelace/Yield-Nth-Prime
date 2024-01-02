def is_prime(n):
    if x ==1: 
        return False 
    for i in range (2,x):
        if x%i==0:
            return False
    else: return True 

def yield_nth_prime():
    n = int (input("Enter n:"))
    #Initialize a counter variable _zero to 0 
    ##and a variable _two to 2, 
    ###which is the first prime number.
    _zero= 0 
    _two = 2 
    #Enter a while loop to check if _two is prime 
    ##using the is_prime function based on _zero's value

    ###if _two IS prime, _zero increases by 1. 
    ####if _zero equals n, then _two is the nth prime number
    #####if _two does not equal n, and it is not prime, 
    ######_zero increases again by 1.
    while _zero < n: 
        if is_prime(_two):
            _zero +=1
        if _zero ==n:
            return _two
        _two+=1


print (nth_prime(7))


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


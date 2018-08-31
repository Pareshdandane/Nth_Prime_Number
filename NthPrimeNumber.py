def isprime(N):
    for i in range(2,int(N**0.5)+1):
        if N % i == 0:
            return False
    return True
        
def nth_prime(N):
    if N==1:
        return 2
    num=3
    count=2
    while count < N:
        num+=2
        if isprime(num):
            count+=1
    return num
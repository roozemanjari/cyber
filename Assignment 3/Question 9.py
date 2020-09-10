def count_primes(num):
    c=0
    for n in range(2,num+1):
        prime=True
        for i in range(2,n):
            if (n%i==0):
                prime=False
                break
        if prime:
            c+=1
    return c

print(count_primes(100))

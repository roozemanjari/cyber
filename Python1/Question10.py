def binomialCoeff(n, k) : 
    res = 1
    if (k > n - k) : 
        k = n - k 
    for i in range(0 , k) : 
        res = res * (n - i) 
        res = res // (i + 1) 
      
    return res
def printPascal(n) : 
      
    for line in range(0, n) : 
        a=[]
        for i in range(0, line + 1) : 
            a.append(binomialCoeff(line, i))
        print(a)
        
printPascal(5)

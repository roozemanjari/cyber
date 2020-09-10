def spy_game(n):
    no_of_zeros=0
    for n in n:
        if no_of_zeros<2 and n==0:
            no_of_zeros+=1
        elif no_of_zeros==2 and n==7:
            return True
    return False    
        

print(spy_game([1,2,4,0,0,7,5]))
print(spy_game([1,0,2,4,0,5,7]))
print(spy_game([1,7,2,0,4,5,0]))  

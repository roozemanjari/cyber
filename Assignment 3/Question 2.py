def lesser_of_two_events(a,b):
    if a%2==0 and b%2==0:
        if a<b:
            return a
        else:
            return b
    else:
        if a<b:
            return b
        else:
            return a
        
print(lesser_of_two_events(2,5))     
print(lesser_of_two_events(2,4))

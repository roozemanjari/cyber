def blackjack(x,y,z):
    sum=x+y+z
    if sum<=21:
        return sum
    elif sum>21 and 11 in [x,y,z]:
        sum=sum-10
        if sum>21:
            return 'BUST'
        else:
            return sum
    else:
        return 'BUST'
    

print(blackjack(5,6,7))
print(blackjack(9,9,9))
print(blackjack(9,9,11)

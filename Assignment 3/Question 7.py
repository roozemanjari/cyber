def summer_69(arr):
    if not arr:
        return 0
    else:
        sum=0
        result=True
        for x in arr:
            if result:
                if x!=6:
                    sum+=x
                else:
                    result=False
                    
            else:
                if x==9:
                    result=True
        return sum            
            

print(summer_69([1,3,5]))
print(summer_69([4,5,6,7,8,9]))
print(summer_69([2,1,6,9,11]))

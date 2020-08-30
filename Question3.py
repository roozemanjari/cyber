def checkString(s):
    u=0
    l=0
    for i in range(0,len(s)):
         if(s[i].isupper()) :
            u=u+1
         else:
            l=l+1
    print"No of lower case letters are %d",l
    print"No of upper case letters are %d",u
checkString("RooZeeEe")

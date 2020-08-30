def prime(n):
  x = ["PRIME"]*(n+1)
  x[0] = x[1]="NOT PRIME"
  for i in range(2,n+1) :
    if (x[i] == "PRIME" and i * i <= n):
        for j in range ( i * i,n+1,i):
            x[j] = "NOT PRIME";
  y = {i:x[i] for i in range(2,n+1)}
  z = {key:val for key, val in y.items() if val != "NOT PRIME"}  
  return len(y)-len(z)


print(prime(7))

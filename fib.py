n = int(input("number: ")) 

a = 0
b = 1
c = 1

if n==0:
    print(0)
elif n < 3:
    print(1) 
else:
    for i in range(1,n-1):
        a = b + c
        b = c
        c = a
    print(a)



#Q 1)

def area():
    pi=22/7
    ra=float(input("Enter radius of sphere="))
    ar=4*(pi*ra**2)
    print(" Area of sphere=",ar) 
area()

#Q 2)

def factors(x):
    return [y for y in range(1, int(x/2)+1) if x%y==0]
 
def perfect(a,b):
    return [x for x in range(a,b+1) if sum(factors(x))==x]
print("Perfect numbers between 1 and 1000",perfect(1, 1000))

#Q 3)

n=int(input("Enter number for multiplication table="))
for i in range(1, 10):
   print(n,"*",i,"=",n*i)
   
#Q 4)

def power(b,p):
    if(p==1):
        return(b)
    if(p!=1):
        return(b*power(b,p-1))  # Here recursion is performed
b=int(input("Enter num "))
p=int(input("Enter power "))
print(" power=",power(b,p))

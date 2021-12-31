
#Factorial Number
def fact(n):
        fac = 1
        for i in range(1,n+1): fac *= i
        return fac

#Number of zeros in the factorial result
def factorial_zeros(n):
    i = 5; count = 0
    while i <= n: 
        count += n//i
        i *= i  
    return count
#2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.

#What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?

def mcd(a,b):    #maximo comun divisor (greatest common divisor)
    return b and mcd(b, a%b) or a 
def mcm(a,b):    #minimo comun multiplo (least common multiple)
    return a*b/mcd(a,b)  # mcm*mcd = |a*b|

n = 1  
for i in range(1, 21):
    n = mcm(n, i)

print(n)
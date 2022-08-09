"""
The sum of the squares of the first ten natural numbers is,

The square of the sum of the first ten natural numbers is,

Hence the difference between the sum of the squares of the first ten natural numbers and the square of the sum is .

Find the difference between the sum of the squares of the first one hundred natural numbers and the square of the sum.

"""

def sum_of_squares(n):
    sum_1 = 0
    for i in range(1, n + 1):
        i = i*i
        sum_1 += i
    return sum_1
        
def square_of_sum(n):
    sum_2 = 0
    for i in range(1, n +1):
        sum_2 += i
    return sum_2*sum_2

difference = sum_of_squares(100) - square_of_sum(100)

print(square_of_sum(100))
print(difference)
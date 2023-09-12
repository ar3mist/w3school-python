#Write a Python program to calculate the sum of three given numbers.
#If the values are equal, return three times their sum.

#anser

def sum_of_three(x,y,z):

    sum = x + y + z

    if x == y == z:
        sum = sum
    return sum

print(sum_of_three(1,2,3))
print(sum_of_three(10,30,40))
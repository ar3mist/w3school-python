#Write a Python program to calculate the difference between a given number and 17.
#If the number is greater than 17, return twice the absolute difference.

def difference(random_number):
    if random_number <= 17:
        return 17 - random_number

    else:
        return  (random_number - 17 ) * 2

print(difference(22))
print(difference(3))


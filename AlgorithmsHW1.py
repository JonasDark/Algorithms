
# 1. COMPUTE THE SUM OF DIGITS FOR ALL NUMBERS FROM 1 TO N.

'''
num = int(input('Enter your number: '))


def sum_num(n):
    return int((n/2) * (1 + n))


print(sum_num(num))
'''

# Success!


# Exercise 2. FIND MAX NUMBER.

'''
num1 = int(input('Enter your 1st of 3 numbers: '))
num2 = int(input('Enter your 2nd of 3 numbers: '))
num3 = int(input('Enter your 3rd and final number: '))


def maximum_num(a, b, c):
    if a > b and a > c:
        return a

    if b > a and b > c:
        return b
    else:
        return c


print(maximum_num(num1, num2, num3))
'''
# Success!


# Exercise 3: COUNT ODD AND EVEN NUMBERS

user_num = int(input("Enter your number: "))


def odd_even_count(num):
    count_even = 0
    count_odd = 0
    while num != 0:
        digi = num % 10
        if digi % 2:
            count_odd += 1
        else:
            count_even += 1
        num = num // 10
    return 'Evens:' + str(count_even) + '\nOdds:' + str(count_odd)


print(odd_even_count(user_num))


# Success! I definitely had difficulty with this one, but now I will know how to approach a problem like this in the future.








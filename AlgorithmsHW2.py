
# EXERCISE 1.
# Given a string. Split it into two equal parts. Swap these parts and return the result.
# If the string has odd characters, the first part should be one character greater than the second part.
# Example: string = 'bbbbbcaaaaa'. Result = ‘aaaaabbbbbc’.

# First Attempt

'''
r = 'bbbbbcaaaaa'

def split_join(n):
    print(n)
    w = n[:6]
    x = n[6:]
    return x + w


print(split_join(r))
'''

# Failed, includes a space

# Second Attempt
'''
r = 'bbbbbcaaaaa'


def split_join2(n):
    print(n)
    if len(n) % 2 != 0:
        first_part = n[:len(n)//2 + 1]
        second_part = n[len(n)//2 + 1:]
        return second_part + first_part
    elif len(n) % 2 == 0:
        first_part = n[:len(n)//2]
        second_part = n[len(n)//2:]
        return second_part + first_part


print(split_join2(r))
'''
# Success, returns original string (for comparison) and also the new split and joined string, no spaces.


# EXERCISE 2

# Unique Characters in String
# Given a string, determine if it consists of all unique characters.
# For example, the string 'abcde' has all unique characters and should return True.
# The string 'aabcde' contains duplicate characters and should return False.


s = 'abcde'


def unique(n):
    t = set(n)
    if len(t) == len(s):
        return True
    else:
        return False


print(unique(s))

# Success! Thanks for the hint!



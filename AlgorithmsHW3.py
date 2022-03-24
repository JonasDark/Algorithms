
#EXERCISE 1 - REVERSE A STATEMENT

'''
text = input('Enter a sentence: ')

list1 = text.split()
backward_list = list1[::-1]
backward_sentence = ' '.join(backward_list)
print(backward_sentence)

# or

print(' '.join(text.split()[::-1]))
'''

#EXERCISE 2 - PERMUTATIONS

'''
text = 'abc'

a = text[0] + text[1] + text[2] + ","
b = text[0] + text[2] + text[1] + ","

c = text[1] + text[0] + text[2] + ","
d = text[1] + text[2] + text[0] + ","

e = text[2] + text[1] + text[0] + ","
f = text[2] + text[0] + text[1]

g = a + b + c + d + e + f
print(g)
'''
# or

'''
def print_permu(a):
    return ' '.join(a)


def permu(text, start, stop):
    if start == stop:
        print(print_permu(text))
    else:
        for i in range(start, stop+1):
            text[start], text[i] = text[i], text[start]
            permu(text, start+1, stop)
            text[start], text[i] = text[i], text[start]


my_text = input('Enter text for permutation: ')

c = list(my_text)
d = len(my_text)
permu(c, 0, d-1)

'''

#EXERCISE 3 - COUNT CHARACTERS

'''
text = input('Please enter your text: ')
text = text.lower()

vowels = 0
non_vowels = 0

for i in text:
    if i == 'a' or i == 'e' or i == 'i' or i == 'o' or i == 'u':
        vowels += 1
    else:
        non_vowels += 1

a = 'Vowels: ' + str(vowels) + ','
b = 'Consonants: ' + str(non_vowels)

print(a, b)

'''
















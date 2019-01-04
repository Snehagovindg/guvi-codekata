c = input().lower()

vowels = ['a', 'e', 'i', 'o', 'u']

if c.isalpha():
    if c in vowels:
        print('Vowel')
    else:
        print('Consonant')
else:
    print('invalid')

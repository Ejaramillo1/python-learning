s = 'emsezpyi'
numVowels = 0
vowels = ['a','e','i','o','u']

for i in range(len(s)):
    if s[i] in vowels:
        numVowels += 1
print("Number of vowels: " + str(numVowels))
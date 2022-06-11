from gettext import find


s = 'azcbobobegghakl'
nBob = 0
for i in range(len(s)):
    if s[i:i+3] == 'bob':
        nBob += 1
print("Number of times bob occurs is: " + str(nBob))

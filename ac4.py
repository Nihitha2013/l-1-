str1 = input("Enter a sentence: ")
n = 1

for x in range(len(str1)):
    if(str1[x] == ' ' ):
        n = n + 1

print("Total Number of words= ",n)
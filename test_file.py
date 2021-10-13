# Finds vowels and consants

words = input("Please enter a word \n")

count = 0

for word in words:
    if word in "aeiou":
        count += 1
print(count)
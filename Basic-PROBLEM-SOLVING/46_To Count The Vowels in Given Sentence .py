sentence = input("Type a sentence here:     ")
s = sentence.lower()
list1 = ["a", "e", "i", "o", "u"]

count = 0
for char in s:
    if char in list1:
        count = count +1

print(count)




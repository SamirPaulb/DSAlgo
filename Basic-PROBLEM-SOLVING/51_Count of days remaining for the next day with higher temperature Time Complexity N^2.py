#i/p: {30,28,31,33,29,27,34}
# Time Complexity is O(N^2)
#o/p: {2, 1, 1, 3, 2, 1, 0}
result = []
temp = [30,28,31,33,29,27,34]
for i in range(len(temp)):
    for j in range(i,len(temp)):
        if temp[i]< temp[j]:
            result.append(j-i)
            break

result.append(0)

print(result)
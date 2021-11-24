# Python Program To Find out the Maximum Value in Nested List
list2 = []
def get_max(list1):
    for i in list1:
        if type(i) == list:
            get_max(i) 
        else:
            list2.append(i)
    return max(list2)

list1 = [1,2,23,[12,1,97,[245,42,[343,45,2,445666],35],3,5,2],53,[3,6],4,[3],4,]

print(get_max(list1))
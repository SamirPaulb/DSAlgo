sub1 = int(input("Write the  subject1 marks: \n"))
sub2 = int(input("Write the  subject2 marks: \n"))
sub3 = int(input("Write the  subject3 marks: \n"))
sub4 = int(input("Write the  subject4 marks: \n"))

if(sub1<33 or sub2<33 or sub3<33):
    print("You are FAIL due to less any subject marks than 33% ")
elif(sub1 + sub2 + sub3 )/3 < 40:
    print("You are FAIL due to avgerage marks is less than 40%") 
else:
    print("PASS")


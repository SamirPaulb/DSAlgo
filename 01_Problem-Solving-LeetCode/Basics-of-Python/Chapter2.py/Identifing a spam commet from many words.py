spam_comments = ["spam","bad","Worst","Not Good","lazy","dog","cat","false"]

a = input("Write a comment here: \n")

if(a in spam_comments):
    print("It Is A SPAM COMMENT")
else:
    print("Good commemt")
    
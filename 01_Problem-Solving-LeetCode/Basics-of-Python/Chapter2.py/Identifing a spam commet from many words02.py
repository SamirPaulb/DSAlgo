text = input("Write a comment here: \n")

if("bad" in text):
    Spam = True
else:
    Spam = False

if("worse" in text):
    Spam = True
else:
    Spam = False

if("money" in text):
    Spam = True
else:
    Spam = False

if("rotten" in text):
    Spam = True
else:
    Spam = False

if(True):
    print("This is a SPAM COMMENT")
else:
    print("Good comment")



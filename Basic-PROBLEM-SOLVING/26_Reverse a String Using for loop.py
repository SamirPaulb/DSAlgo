def reverse(string):
    rev_string = ""
    for i in string:
        rev_string  = i + rev_string
    print(rev_string)

string = input("--->>")
reverse(string)

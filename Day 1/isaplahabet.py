def isaplha(a):
    if a in "abcdefghijklmnopqrstuvwxyzAQWERTYUIOPSDFGHJKLZXCVBNM":
        return ("IS ALPHABET")
    else:
        return ("NOT ALPHABET")

a=input("Enter a alphabet")
print("THE EBTERED CHARACTER IS",isaplha(a))
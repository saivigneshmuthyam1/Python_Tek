def vc(a):
    if a in "aeiouAEIOU":
        return "VOWELS"
    else:
        return "CONSONANT"
    
a=input("ENTER A ALPHABET")
print("alphabet",a,"is",vc(a))
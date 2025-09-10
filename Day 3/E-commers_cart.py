def choice(l,a):
    if a==1:
        print("Enter product to add:")
        Add_product(l,input())
        return True
    elif a==2:
        Remove_pro(l,input("Enter the product ro remove"))
        return True
    elif a==3:
        b=input("Enter Element to search")
        x=Search_pro(l,b)
        if x:
            print(f"Yes, {b} is in the cart.")
        else:
            print(f"{b} is not in the cart.")
        return True
    elif a==4:
        display(l)
        return True
    elif a==5:
        count(l)
        return True
    elif a==6:
        print(f"Sorted cart:{l.sort()}")
    elif a==7 :
        l.clear()
        print("List is Cleared")
    else:
        return False
        

def Add_product(l,a):
    l.append(a)

def Remove_pro(l,a):
    try:
        l.remove(a)
        print(f"Product {a} removed from cart.")
    except:
        print(f"Product {a} not avaliable in cart.")

def Search_pro(l,a):
    for i in range(len(a)):
        if l[i]==a:
            return True
    return False

def display(l):
    print("Cart:",end="")
    print(l)

def count(l):
    print("Toatal products in cart:",len(l))

l=[]
q=True
while(q):
    a=int(input("Cart Operations:\n 1. Add Product \n2. Remove Product\n3. Search Product\n4. Display Cart\n5. Count Products\n6. Sort The List\n 7.Clear the Cart\n 8. Exit "))
    q=choice(l,a)
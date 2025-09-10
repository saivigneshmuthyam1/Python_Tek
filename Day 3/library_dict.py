def choice(library,a):
    if a==1:
        add_book(input("Enter Book Id"),input("Enter book Title"))
        return True
    elif a==2:
        remove_book(input("Enter Book Id"))
        return True
    elif a==3:
        search_by_id(input("Enter Book Id to Search"))
        return True
    elif a==4:
        update_title(input("Enter The Book Id "),input("Enter The New Book Title"))
        return True
    elif a==6:
        count_books()
        return True
    elif a==5:
        display_all_books()
        return True
    elif a==7:
        title_exists(input("Enter the title to search"))
    else:
        return False

        
    


    

def add_book(book_id, title):
    if book_id in library:
        print(f"Book ID {book_id} already exists.")
    else:
        library[book_id] = title
        print("Book added.")

def remove_book(book_id):
    if book_id in library:
        del library[book_id]
        print("Book removed.")
    else:
        print("Book ID not found.")

def search_by_id(book_id):
    if book_id in library:
        print(f"Book ID: {book_id}, Title: {library[book_id]}")
    else:
        print("Book ID not found.")

def update_title(book_id, new_title):
    if book_id in library:
        library[book_id] = new_title
        print("Book title updated.")    
    else:
        print("Book ID not found.")

def count_books():
    print(f"Total books: {len(library)}")

def display_all_books():
    if not library:
        print("Library is empty.")
    else:
        for book_id, title in library.items():
            print(f"Book ID: {book_id}, Title: {title}")

def title_exists(title):
    if title in library.values():
        print(f'Title "{title}" exists in the library.')
    else:
        print(f'Title "{title}" does not exist in the library.')



q=True
library={}
while(q):
    a=int(input("1.Add Book \n2.Remove Book\n3.Search for a book\n4.Update the Title\n5.Display all Books\n6.Count the total number of books\n7.Check if a book title exists\n"))
    q=choice(library,a)
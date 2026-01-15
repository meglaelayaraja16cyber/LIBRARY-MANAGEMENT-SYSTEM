# LIBRARY MANAGEMENT SYSTEM - PURE PYTHON (MENU DRIVEN)

library = {}

def add_book():
    book_id = input("Enter Book ID: ")
    if book_id in library:
        print("Book already exists!")
        return
    title = input("Enter Book Title: ")
    author = input("Enter Author Name: ")
    copies = int(input("Enter Number of Copies: "))
    library[book_id] = {
        "title": title,
        "author": author,
        "copies": copies
    }
    print("Book added successfully.")

def view_books():
    if not library:
        print("No books available.")
        return
    print("\n--- Available Books ---")
    for book_id, details in library.items():
        print("ID:", book_id,
              "| Title:", details["title"],
              "| Author:", details["author"],
              "| Copies:", details["copies"])

def issue_book():
    book_id = input("Enter Book ID to Issue: ")
    if book_id not in library:
        print("Book not found!")
        return
    if library[book_id]["copies"] > 0:
        library[book_id]["copies"] -= 1
        print("Book issued successfully.")
    else:
        print("No copies available.")

def return_book():
    book_id = input("Enter Book ID to Return: ")
    if book_id not in library:
        print("Book not found!")
        return
    library[book_id]["copies"] += 1
    print("Book returned successfully.")

def search_book():
    book_id = input("Enter Book ID to Search: ")
    if book_id in library:
        details = library[book_id]
        print("Book Found:")
        print("Title:", details["title"])
        print("Author:", details["author"])
        print("Copies:", details["copies"])
    else:
        print("Book not found!")

while True:
    print("\n===== LIBRARY MANAGEMENT SYSTEM =====")
    print("1. Add Book")
    print("2. View Books")
    print("3. Issue Book")
    print("4. Return Book")
    print("5. Search Book")
    print("6. Exit")

    choice = input("Enter your choice (1-6): ")

    if choice == "1":
        add_book()
    elif choice == "2":
        view_books()
    elif choice == "3":
        issue_book()
    elif choice == "4":
        return_book()
    elif choice == "5":
        search_book()
    elif choice == "6":
        print("Thank you for using Library Management System.")
        break
    else:
        print("Invalid choice! Please try again.")

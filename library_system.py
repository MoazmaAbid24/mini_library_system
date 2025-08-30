import json
import os

FILE_NAME = "library.json"

# Load books from file
def load_books():
    if os.path.exists(FILE_NAME):
        with open(FILE_NAME, "r") as f:
            return json.load(f)
    return []

# Save books to file
def save_books(books):
    with open(FILE_NAME, "w") as f:
        json.dump(books, f, indent=4)

# Add a new book
def add_book(books):
    book_id = input("Enter Book ID: ")
    # Check if Book ID already exists
    for book in books:
        if book["id"] == book_id:
            print("❌ Book ID already exists!")
            return
    title = input("Enter Book Title: ")
    author = input("Enter Author Name: ")
    quantity = int(input("Enter Quantity: "))
    books.append({"id": book_id, "title": title, "author": author, "quantity": quantity})
    save_books(books)
    print("✅ Book added successfully!")

# View all books
def view_books(books):
    if not books:
        print("⚠️ No books available!")
        return
    print("\n===== Available Books =====")
    for book in books:
        print(f"ID: {book['id']}, Title: {book['title']}, Author: {book['author']}, Quantity: {book['quantity']}")
    print("============================")

# Borrow a book
def borrow_book(books):
    book_id = input("Enter Book ID to borrow: ")
    for book in books:
        if book["id"] == book_id:
            if book["quantity"] > 0:
                book["quantity"] -= 1
                save_books(books)
                print(f"✅ You borrowed '{book['title']}'")
            else:
                print("❌ Book not available right now!")
            return
    print("❌ Book ID not found!")

# Return a book
def return_book(books):
    book_id = input("Enter Book ID to return: ")
    for book in books:
        if book["id"] == book_id:
            book["quantity"] += 1
            save_books(books)
            print(f"✅ You returned '{book['title']}'")
            return
    print("❌ Book ID not found!")

# Main Menu
def main():
    books = load_books()
    while True:
        print("\n===== Mini Library Management System =====")
        print("1. Add Book")
        print("2. View All Books")
        print("3. Borrow Book")
        print("4. Return Book")
        print("5. Exit")
        choice = input("Enter your choice: ")

        if choice == "1":
            add_book(books)
        elif choice == "2":
            view_books(books)
        elif choice == "3":
            borrow_book(books)
        elif choice == "4":
            return_book(books)
        elif choice == "5":
            print("👋 Exiting program...")
            break
        else:
            print("⚠️ Invalid choice! Try again.")

if __name__ == "__main__":
    main()

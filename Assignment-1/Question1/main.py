import datetime

def add_book():
    book_id = input("Enter book ID: ")
    title = input("Enter title: ")
    author = input("Enter author: ")
    publication_year = input("Enter publication year: ")
    with open("books.txt", "a") as f:
        f.write(f"{book_id},{title},{author},{publication_year}\n")

def add_user():
    user_id = input("Enter user ID: ")
    name = input("Enter name: ")
    address = input("Enter address: ")
    phone_number = input("Enter phone number: ")
    with open("users.txt", "a") as f:
        f.write(f"{user_id},{name},{address},{phone_number}\n")

def issue_book():
    book_id = input("Enter book ID: ")
    user_id = input("Enter user ID: ")
    issue_date = datetime.datetime.now().strftime("%Y-%m-%d")
    with open("transactions.txt", "a") as f:
        f.write(f"{len(open('transactions.txt').readlines()) + 1},{book_id},{user_id},{issue_date},\n")

def return_book():
    transaction_id = int(input("Enter transaction ID: "))
    with open("transactions.txt", "r+") as f:
        lines = f.readlines()
        for i, line in enumerate(lines):
            if str(transaction_id) in line:
                lines[i] = line.strip() + f",{datetime.datetime.now().strftime('%Y-%m-%d')}\n"
                break
        f.seek(0)
        f.writelines(lines)


while True:
    print("1. Add Book")
    print("2. Add User")
    print("3. Issue Book")
    print("4. Return Book")
    print("5. Exit")
    choice = int(input("Enter your choice: "))
    if choice == 1:
        add_book()
    elif choice == 2:
        add_user()
    elif choice == 3:
        issue_book()
    elif choice == 4:
        return_book()
    elif choice == 5:
        break
    else:
        print("Invalid choice")

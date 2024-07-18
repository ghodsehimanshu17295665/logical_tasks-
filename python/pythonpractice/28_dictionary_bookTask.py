def add_book_detail():
    collection = {}

    while True:
        title = input("Enter Book's Title: ")
        author = input("Enter Author's Name: ")
        genere = input("Enter Book's Genre: ")
        date = input("Enter Book's published Date: ")

        collection[title] = {
            "Author's Name": author,
            "Book's Genre": genere,
            "Book's published Date": date,
        }

        more_details = input("Do you want to Enter more Details? (Y/N): ")
        if more_details != "Yy":
            break
    return collection


books = add_book_detail()
print(books)

from books.books import Book

# Create book and save into DB
python_guide = Book()
python_guide.title = 'Python Guide'
python_guide.author = 'python.org'
python_guide.save()

print(python_guide.id)

# Update book and save changes into DB
python_guide.author = 'Guido Van Rossum'
python_guide.save()

print(python_guide.id)
print(python_guide.author)

# Retrieve book from db
book = Book(1)
print(book.id)
print(book.title)
print(book.author)

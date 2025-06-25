# Library Management System

A simple Python-based library management system that allows you to manage books in a digital library.

## Features

- **Book Management**: Create and store book objects with title, author, and ISBN
- **Library Operations**: Add books, remove books, and display library contents
- **Book Information**: Display detailed information about each book

## Classes

### Book Class
Represents a book with the following attributes:
- `title`: The title of the book
- `author`: The author of the book  
- `isd`: The ISBN (book identifier)

**Methods:**
- `info()`: Displays book information (title, author, ISBN)

### Library Class
Represents a library that can hold multiple books.

**Attributes:**
- `name`: Name of the library
- `books`: List of books in the library

**Methods:**
- `add_book(book)`: Adds a book to the library
- `remove_book(isd1)`: Removes a book by ISBN
- `display()`: Shows all books in the library

## Usage Example

```python
# Create books
b1 = book("physics", "HC verma", "123245")
b2 = book("maths", "S dey", "2454764")

# Create library
l1 = library("digital_library")

# Add books to library
l1.add_book(b1)
l1.add_book(b2)

# Display library contents
l1.display()
```

## Sample Output

```
Author HC verma is added to your library
Author S dey is added to your library
books in digital_library is
physics HC verma 123245
maths S dey 2454764
```

## Installation

1. Clone this repository:
```bash
git clone https://github.com/yourusername/library-management-system.git
```

2. Navigate to the project directory:
```bash
cd library-management-system
```

3. Run the Python script:
```bash
python library_system.py
```

## Requirements

- Python 3.x

## Known Issues & Fixes Needed

The current code has several bugs that need to be addressed:

1. **Book class initialization**: The `self.author=author` line is outside the `__init__` method
2. **Missing closing parenthesis** in the `info()` method print statement
3. **Variable name error** in `remove_book()`: should be `self.books` instead of `books`
4. **String formatting error**: `.formet` should be `.format(isd1=isd1)` or use f-string
5. **Class naming**: Should follow PascalCase convention (`Book`, `Library`)

## Contributing

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/improvement`)
3. Commit your changes (`git commit -am 'Add some improvement'`)
4. Push to the branch (`git push origin feature/improvement`)
5. Create a Pull Request

## Future Enhancements

- Add search functionality by title or author
- Implement book borrowing/return system
- Add data persistence (save/load from file)
- Include book categories and tags
- Add user management system

## License

This project is open source and available under the [MIT License](LICENSE).

## Contact

For questions or suggestions, please open an issue on GitHub.

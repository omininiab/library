let myLibrary = [{ title: "Art of war", author: "Sun Tzu", read: false}];

class Book {
    constructor(title, author, read) {
        // the constructor...
        this.title = title; // String
        this.author = author; // String
        this.read = read; // Boolean
    }
    changeReadStatus() {
        this.read = Boolean(1 - this.read);
    }
}

function addBookToLibrary() {
    addBook = document.getElementById("addBook")
    
    myLibrary.push(book)
    displayBooks()
}

function removeBookFromLibrary() {
    //myLibrary.push(book)
    displayBooks()
}

function displayBooks() {
    myBooks = document.getElementById("myBooks")
    header = document.createElement("h2")
    header.innerText = "My Books"
    list = document.createElement("ol")
    if (myLibrary.length > 0) {
        myBooks.appendChild(header)
        myBooks.appendChild(list)

        i = 0;
        myLibrary.forEach(function (book) {
            console.log(book)
            myBook = document.createElement("li")
            myBook.innerText = `${book["title"]} by ${book["author"]}`
            list.appendChild(myBook)
            i++
        })
    } else {
        warning = document.createElement("p")
        warning.innerText = "You haven't listed any books yet."
        myBooks.appendChild(warning)
    }
}

displayBooks()
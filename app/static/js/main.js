function deleteBook(bookID) {
    fetch("/delete-book", {
        method: "POST",
        body: JSON.stringify({ bookID: bookID }),
    }).then((_res) => {
        window.location.href = "/";
    });
}


let myLibrary = [{ title: "Art of war", author: "Sun Tzu", read: false }, { title: "Prisoners of Geography", author: "Tim Marshall", read: true }, { title: "Antisocial", author: "Samuel Ominini", read: true }, { title: "Web Development", author: "Quincy Larson", read: false }];

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

addBook = document.getElementById("addBook")
addBook.onsubmit = function () {
    title = document.getElementById("title")
    author = document.getElementById("author")
    readStatus = document.getElementsByName("readStatus")
    bookTitle = title.value
    bookAuthor = author.value
    for (let i = 0; i < readStatus.length; i++) {
        if (readStatus[i].checked) {
            bookReadStatus = Boolean(readStatus[i].value)
        }
    }

    myLibrary.push(new Book(bookTitle, bookAuthor, bookReadStatus))
    addBook.reset();

    displayBooks()
    return false
}

function removeBookFromLibrary() {
    //myLibrary.push(book)
    displayBooks()
}

function displayBooks() {
    myBooks = document.getElementById("myBooks")
    myBooks.innerHTML = ""
    header = document.createElement("h2")
    header.innerText = "My Books"
    books = document.createElement("div")
    books.classList.add("w3-container")
    books.id = "books"


    if (myLibrary.length > 0) {
        myBooks.appendChild(header)
        myBooks.appendChild(books)

        myLibrary.forEach(function (book) {
            card = document.createElement("div")
            card.classList.add("w3-card-4")
            card.classList.add("book")
            books.appendChild(card)
            console.log(book)
            myBook = document.createElement("p")
            myBook.classList.add("bookInfo")
            myBook.classList.add("w3-monospace")
            myBook.innerText = `${book["title"]} by ${book["author"]}`
            switcher = document.createElement("label")
            switcher.classList.add("switch")
            checkbox = document.createElement("input")
            checkbox.type = "checkbox"
            checkbox.checked = book["read"]
            slider = document.createElement("span")
            slider.classList.add("slider")
            switcher.appendChild(checkbox)
            switcher.appendChild(slider)
            card.appendChild(myBook)
            card.appendChild(switcher)
        })
    } else {
        warning = document.createElement("p")
        warning.innerText = "You haven't listed any books yet."
        myBooks.appendChild(warning)
    }
}

displayBooks()
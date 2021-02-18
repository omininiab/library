function navbar() {
    var x = document.getElementById("demo");
    if (x.className.indexOf("w3-show") == -1) {
        x.className += " w3-show";
    } else {
        x.className = x.className.replace(" w3-show", "");
    }
}

function deleteBook(bookID) {
    card = document.getElementById(bookID)
    card.parentElement.style.display = 'none';
    fetch("/delete-book", {
        method: "POST",
        body: JSON.stringify({ bookID: bookID }),
    }).then((_res) => {
        window.location.href = "/";
    });
}

function updateBook(bookID) {

}
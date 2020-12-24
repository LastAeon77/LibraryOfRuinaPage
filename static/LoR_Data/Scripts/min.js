var Deckfilter = () => {
    let stuff = document.getElementById("Rank");
    let strUser = stuff.value;
    let allRows = document.getElementsByTagName("tr")
    Array.prototype.forEach.call(allRows, (stuff) => {
        if (strUser === "any") {
            stuff.style.display = ""
        }
        else {
            if (stuff.id !== strUser) {
                stuff.style.display = "none"
            }
            if (stuff.id === strUser) {
                stuff.style.display = ""
            }
        }
        if (stuff.id === "") {
            stuff.style.display = ""
        }
    }
    )

}


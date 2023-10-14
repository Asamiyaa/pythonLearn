document.getElementById("showContentLink").addEventListener("click", function(event) {
    event.preventDefault(); // Prevent the link's default behavior (e.g., jumping to a new page)

    var hiddenContent = document.querySelector(".hidden-content");
    if (hiddenContent.style.display === "none" || hiddenContent.style.display === "") {
        hiddenContent.style.display = "block";
    } else {
        hiddenContent.style.display = "none";
    }
});

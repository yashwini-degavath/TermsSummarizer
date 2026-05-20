function uploadFile() {
    let fileInput = document.getElementById("pdfFile");
    let file = fileInput.files[0];

    if (!file) {
        alert("Please select a file.");
        return;
    }

    let formData = new FormData();
    formData.append("file", file);

    fetch("http://127.0.0.1:5000/summarize", {
        method: "POST",
        body: formData
    })
    .then(response => response.json())
    .then(data => {
        document.getElementById("summary").innerText = data.summary;
    })
    .catch(error => {
        console.error("Error:", error);
    });
}

function translateText() {

    let text = document.getElementById("inputText").value;
    let source = document.getElementById("source").value;
    let target = document.getElementById("target").value;

    fetch("/translate", {
        method: "POST",
        headers: {
            "Content-Type":"application/json"
        },
        body: JSON.stringify({
            text:text,
            source:source,
            target:target
        })
    })

    .then(response => response.json())

    .then(data => {
        document.getElementById("outputText").value = data.translated;
    });

}
document.getElementById('text-form').addEventListener('submit', function(event) {
    event.preventDefault();
    const text = document.getElementById('text-input').value;
    fetch('/process', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
        },
        body: JSON.stringify({ text: text }),
    })
    .then(response => response.json())
    .then(data => {
        let result = '<h2>Processed Text</h2>';
        result += '<p>Cleaned Text: ' + data.cleaned_text + '</p>';
        result += '<p>Sentences: ' + data.sentences.join('<br>') + '</p>';
        result += '<p>Tokenized Sentences: ' + JSON.stringify(data.tokenized_sentences) + '</p>';
        document.getElementById('result').innerHTML = result;
    });
});

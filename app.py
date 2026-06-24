from flask import Flask, render_template, request, jsonify
from deep_translator import GoogleTranslator

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/translate', methods=['POST'])
def translate():
    data = request.json

    text = data['text']
    source = data['source']
    target = data['target']
    
    print("Text:", text)
    print("Source:", source)
    print("Target:", target)
    
    translated = GoogleTranslator(
        source=source,
        target=target
    ).translate(text)

    return jsonify({"translated": translated})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
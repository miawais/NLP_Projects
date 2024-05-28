# app/routes.py
from flask import request, render_template, jsonify
from flask import current_app as app
from . import utils

@app.route('/')
def index():
    return render_template(r'D:\\NLP_Projects\\WordPredictor\\templates\\index.html')


@app.route('/process', methods=['POST'])
def process():
    text = request.form['text']
    cleaned_text = utils.remove_undecodable_characters(text)
    sentences = utils.split_to_sentences(cleaned_text)
    tokenized_sentences = utils.tokenize_sentences(sentences)
    result = {
        'cleaned_text': cleaned_text,
        'sentences': sentences,
        'tokenized_sentences': tokenized_sentences
    }
    return jsonify(result)

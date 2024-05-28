import re
import nltk
nltk.download('punkt')

def remove_undecodable_characters(text):
    undecodable_pattern = re.compile(r'[^\x00-\x7F]')
    return undecodable_pattern.sub(r'', text)

def split_to_sentences(data):
    sentences = data.split('\n')
    sentences = [s.strip() for s in sentences if s.strip()]
    return sentences

def tokenize_sentences(sentences):
    tokenized_sentences = []
    for sentence in sentences:
        sentence = sentence.lower()
        tokenized = nltk.word_tokenize(sentence)
        tokenized_sentences.append(tokenized)
    return tokenized_sentences

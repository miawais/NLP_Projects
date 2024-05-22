import re

def remove_undecodable_characters(text):
    undecodable_pattern = re.compile(r'[^\x00-\x7F]')
    return undecodable_pattern.sub(r'', text)

def preprocess_data(file_path, output_path):
    with open(file_path, 'r', encoding='utf-8', errors='ignore') as f:
        text = f.read()
    
    clean_text = remove_undecodable_characters(text)
    
    with open(output_path, 'w', encoding='utf-8') as file:
        file.write(clean_text)

if __name__ == "__main__":
    file_path = 'D:\\NLP_Project_01\\project\\data\\twitter.txt'
    output_path = 'D:\\NLP_Project_01\\project\\data\\cleaned_twitter.txt'
    preprocess_data(file_path, output_path)

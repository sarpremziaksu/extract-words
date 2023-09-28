def extract_words(input_string):
    words = [input_string[start:space_index] for start, space_index in enumerate(input_string.split(' '))]
    return words
 
sentence ="Ikinci sektorde sari bayraklar var ve Sebastian Vettel bariyerlerde"
result_words = extract_words(sentence)
print(result_words)

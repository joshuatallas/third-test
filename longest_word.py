

def top_5_longest_words_from_file(words_new.txt):

    with open('words_new.txt', 'r') as f:
        content = file.read()
        words = content.split()

    top_words = sorted(words, key=len, reverse=True)[:5]
return top_words

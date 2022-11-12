path = 'data.txt'
text = open(path).read().lower()
print('length of the corpus is: :', len(text))
unique_words = np.unique(words)
unique_word_index = dict((c, i) for i, c in enumerate(unique_words))
unique_words = np.unique(words)
unique_word_index = dict((c, i) for i, c in enumerate(unique_words))

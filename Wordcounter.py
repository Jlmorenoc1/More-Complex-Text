text = input("What is the text you would like to know the number of words in? Type it here:")

words = text.split()
words_count = len(words)
char = len(text)

awl = words_count/char
print ("words: ", words)
print ("words_count: ", words_count)
print ("char: ", char)
print ("awl: ", awl)
from sys import argv 

def count_words(filename):
    filename = open(filename)
  
    word_occurrences = {}

    for line in filename:
        line = line.rstrip()
        line = line.lower()
        line = line.rstrip('.')
        line = line.replace(",", "")
        line = line.replace("?", "")
        #remove commas
        #print words   
        words = line.split(" ")


    #each word in lists of stripped words
        for word in words:
            word_occurrences[word] = word_occurrences.get(word, 0) + 1

    for key, value in word_occurrences.items():
        print "{} {}".format(key, value)

# count_words("test.txt")

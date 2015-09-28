

#instantiate a dictionary that's gonna hold each new word as a key (dictionaryname.keys=stuff in that other list)

#for every key in the dictionary, += that value each time it's in the master list 

#for key in dictionary, print key, value

def count_words(ourtextfile):
    fileobject = open(ourtextfile)
    masterlist = []
    word_counter = {}
    for line in fileobject:
        words = line.split(" ")
        for word in words:
            word = word.lower().rstrip().rstrip("!.,?")
            masterlist.append(word)
            if word in word_counter:
                word_counter[word] = word_counter[word]+1
            else:
                word_counter[word] = 1
    # print word_counter, "DICT OF WORDS"
    return word_counter

my_tallies = count_words("test.txt")
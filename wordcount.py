

#instantiate a dictionary that's gonna hold each new word as a key (dictionaryname.keys=stuff in that other list)

#for every key in the dictionary, += that value each time it's in the master list 

#for key in dictionary, print key, value

def wordcounter(ourtextfile):
    fileobject = open(ourtextfile)
    masterlist = []
    dict_of_words = {}
    for line in fileobject:
        list_of_words = line.split(" ")
        for word in list_of_words:
            word = word.lower().rstrip().rstrip("!.,?")
            masterlist.append(word)
            dict_of_words[word]=0
    print masterlist, "MASTERLIST"
    for uniqueword in dict_of_words:
        for i in masterlist:
            if i == uniqueword:
                dict_of_words[uniqueword]+=1
        print dict_of_words[uniqueword], uniqueword
    # print dict_of_words, "DICT OF WORDS"
    return 10

wordcounter("test.txt")
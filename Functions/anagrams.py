def anagrams(word, words):
    isit = True
    i = 0
    if len(word) == len(words): 
        for i in word: 
            if word.count(i)!=words.count(i): isit = False
    else: False
    return isit
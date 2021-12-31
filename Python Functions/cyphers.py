# A Vigenere object that works as and advanced cesar cypher that takes a word as key.
class VigenereCipher(object):

    def __init__(self, key, alphabet):
        self.alph = alphabet
        self.keys = [alphabet.find(key[i]) for i in range(len(key))]
        print(self.keys)

    def encode(self, text):
        out =""
        pointer = 0
        for i in text:
            if pointer > len(self.keys)-1: pointer = 0
            #It is not in the alphabet
            ni = self.alph.find(i)
            if ni < 0: 
                out+=i
                pointer+=1
                continue
            
            #It is in the alphabet
            ni += self.keys[pointer]
            if ni > len(self.alph)-1: ni -= len(self.alph)
            out += self.alph[ni]

            pointer += 1
            
        return out
    
    def decode(self, text):
        out = ""
        pointer = 0
        for i in text:
            if pointer > len(self.keys)-1: pointer = 0
            #It is not in the alphabet
            ni = self.alph.find(i)
            if ni < 0: 
                out+=i
                pointer+=1
                continue
            
            #It is in the alphabet
            ni -= self.keys[pointer]
            if ni < -(len(self.alph)-1): ni += len(self.alph)
            out += self.alph[ni]

            pointer += 1
            
        return out

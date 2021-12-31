#Rot13--Cesar  cypher with key==13

def rot13(message):
    alph_low = "abcdefghijklmnopqrstuvwxyz"
    alph_up = alph_low.upper()
    code_low = alph_low[13:] + alph_low[:13]
    code_up = code_low.upper()
    output = ""
    for i in range(len(message)): 
        if alph_low.find(message[i]) >= 0: 
            output += code_low[alph_low.find(message[i])]
        elif alph_up.find(message[i]) >=0: 
            output += code_up[alph_up.find(message[i])]
        else: output += message[i]
    return output

#Useful for later reference in a cesar cypher 
def camel_case(string):
    #your code here
    out = ""
    i = 0
    while i<len(string): 
        if i ==0: 
            out+=string[i].upper()
        elif string[i-1]==" ": out+=string[i].upper()
        else: out+=string[i]
        i+=1
    return out.replace(" ","") 
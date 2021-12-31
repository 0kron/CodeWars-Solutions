#First Option
def valid_parentheses(string):
    if string.count("(") == string.count(")"): 
        for i in range(len(string)): 
            if string[i] == "(": 
                if string[i:].find(")") < 0: return False
            elif string[i] == ")": 
                if string[:i].find("(") < 0: return False
        return True
    return False


#Second point of view
def paremtheses2(x):
    p=[]
    q=[]
    if x.count('(')==x.count(')'):
        for i in range(len(x)):
            if x[i]=='(':
                p.append(i)
            elif x[i]==')':
                q.append(i)
        dic={p[i]:q[i] for i in range(len(p))}
        t=True
        for i in p:
            if i>=dic[i]:
                t=False
        if t==False:           
            print("It's not correct.")
        else:
            print('It is correct.')
    else:
        print("It's not correct.")
import nltk
from nltk import word_tokenize
import six


#Ngram Functions
def vicgram(token, varType, n):
    new = []
    if(varType == 'string'):
        token = word_tokenize(token)
        for x in range(0,len(token) - 2):
            if(n == 1):
                new.append(token[x])
            if(n == 2):
                new.append(token[x] + ',' + token[x+1])
            if(n == 3):
                new.append(token[x] + ',' + token[x+1] + ',' + token[x+2] + ',')
            if(n == 4):
                new.append(token[x] + ',' + token[x+1] + ',' + token[x+2] + ',' + token[x+3] + ',')
            if(n == 5):
                new.append(token[x] + ',' + token[x+1] + ',' + token[x+2] + ',' + token[x+3] + ',' + token[x+4] + ',')
    if(varType == 'tokenized'):
        for x in range(0,len(token) - 2):
            if(n == 1):
                new.append(token[x])
            if(n == 2):
                new.append(token[x] + ',' + token[x+1])
            if(n == 3):
                new.append(token[x] + ',' + token[x+1] + ',' + token[x+2] + ',')
            if(n == 4):
                new.append(token[x] + ',' + token[x+1] + ',' + token[x+2] + ',' + token[x+3] + ',')
            if(n == 5):
                new.append(token[x] + ',' + token[x+1] + ',' + token[x+2] + ',' + token[x+3] + ',' + token[x+4] + ',')
    if(varType == 'integer'):
        token = str(token)
        for x in range(0,len(token) - 2):
            if(n == 1):
                new.append(token[x])
            if(n == 2):
                new.append(token[x] + ',' + token[x+1])
            if(n == 3):
                new.append(token[x] + ',' + token[x+1] + ',' + token[x+2] + ',')
            if(n == 4):
                new.append(token[x] + ',' + token[x+1] + ',' + token[x+2] + ',' + token[x+3] + ',')
            if(n == 5):
                new.append(token[x] + ',' + token[x+1] + ',' + token[x+2] + ',' + token[x+3] + ',' + token[x+4] + ',')
    elif(varType != 'integer' or varType != 'string' or varType != 'token'):
        print("Invalid variable type, Error: " + "'" + varType + "'" + " is not a valid variable type")

        
    return(new)   

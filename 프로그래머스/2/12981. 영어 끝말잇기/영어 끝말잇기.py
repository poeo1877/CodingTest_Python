import math

def solution(n, words):
    beforeWord = words[0]
    person, when  = 0, 0
    
    saidWords = set()
    saidWords.add(beforeWord)

    for index in range(1, len(words)):
        if (words[index][0] != beforeWord[-1] or
                words[index] in saidWords):
            person = n if (index+1) % n == 0 else (index+1) % n
            when = math.ceil((index+1) / n)         #차례
            return [person, when]
        
        saidWords.add(beforeWord)
        beforeWord = words[index]
    
    
    return [0, 0]
__author__ = 'JxKing'
# Given a digit string, return all possible letter combinations that the number could represent.
#
# A mapping of digit to letters (just like on the telephone buttons) is given below. like the telephone buttons
#
#
#
# Input:Digit string "23"
# Output: ["ad", "ae", "af", "bd", "be", "bf", "cd", "ce", "cf"].
#
def letterCombinations(digits):
    """
    :type digits: str
    :rtype: List[str]
    """
        if len(digits)==0 or digits=='1':
            return []
        dict1={}
        dict1['2']=['a','b','c']
        dict1['3']=['d','e','f']
        dict1['4']=['g','h','i']
        dict1['5']=['j','k','l']
        dict1['6']=['m','n','o']
        dict1['7']=['p','q','r','s']
        dict1['8']=['t','u','v']
        dict1['9']=['w','x','y','z']
        dict1['1']=['']
        dict1['0']=[' ']
        pattern={}
        pattern[0]=['']
        length=0
        digits=list(digits)
        n=len(digits)
        while digits:
            digit=digits.pop()
            length+=1
            pattern[length]=[]
            for word in dict1[digit]:
                for j in pattern[length-1]:
                    pattern[length].append(str(word+j))
        return pattern[length]

print(letterCombinations('23'))
print(letterCombinations('1'))
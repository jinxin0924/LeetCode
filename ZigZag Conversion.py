__author__ = 'JxKing'
# The string "PAYPALISHIRING" is written in a zigzag pattern on a given number
# of rows like this: (you may want to display this pattern in a fixed font for better legibility)
#
# P   A   H   N
# A P L S I I G
# Y   I   R
# And then read line by line: "PAHNAPLSIIGYIR"
# Write the code that will take a string and make this conversion given a number of rows:
#
# string convert(string text, int nRows);
# convert("PAYPALISHIRING", 3) should return "PAHNAPLSIIGYIR".

def convert( s, numRows):
    """
    :type s: str
    :type numRows: int
    :rtype: str
    """
    if len(s)<=numRows or numRows==1:return s #special case
    wordlist=['' for i in range(numRows)] #record word in each row
    num_row=0
    direction=-1 #to represent the change for zigzag
    for word in s:
        wordlist[num_row]+=word
        if num_row==0 or num_row==numRows-1:
            direction*=-1
        num_row+=direction
    string=''
    for words in wordlist:
        string+=words
    return string
print(convert("PAYPALISHIRING", 3))
print(convert("AB", 1))
print(convert("", 1))
print(convert("ABC", 2))
#
def convert( s, numRows):
    if numRows == 1 or numRows >= len(s): return s
    final = [[] for row in range(numRows)]
    for i in range(len(s)):
        final[numRows -1 - abs(numRows - 1 - i % (2 * numRows - 2))].append(s[i]) #calculate the index
    return "".join(["".join(final[i]) for i in range(numRows)])

print(convert('abcdef',2))
print(convert("PAYPALISHIRING", 3))
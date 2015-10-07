__author__ = 'JxKing'
# pattern = "abba", str = "dog cat cat dog" should return true.
# pattern = "abba", str = "dog cat cat fish" should return false.

def wordPattern(pattern, str):
    """
    :type pattern: str
    :type str: str
    :rtype: bool
    """
    str_list=str.split()
    if len(str_list) != len(pattern):
        return False
    dict1={} #record the relation from pattern to str
    dict2={} #record the relation from str to pattern
    for i in range(len(pattern)):#traverse to check whether there is conflict or duplicate
        if pattern[i] not in dict1:
            dict1[pattern[i]]=str_list[i]
        else:
            if dict1[pattern[i]] !=str_list[i]:
                return False
        if str_list[i] not in dict2:
            dict2[str_list[i]]=pattern[i]
        else:
            if dict2[str_list[i]]!=pattern[i]:
                return False
    return True
print(wordPattern("abba","dog cat cat dog"))
print(wordPattern("abba","dog cat cat fish"))
print(wordPattern("aaaa","dog cat cat dog"))
print(wordPattern("abba","dog dog dog dog"))

def wordPattern(pattern, str):
    str_list=str.split()
    if len(str_list) != len(pattern):
        return False
    pts={} #record the relation from pattern to str
    stp={} #record the relation from str to pattern
    for patt,word in zip(pattern,str_list):#Use zip to make several i-th element as set
        if patt not in pts:
            pts[patt]=word
        if word not in stp:
            stp[word]=patt
        if pts[patt] !=word or stp[word]!=patt:
            return False
    return True
print(wordPattern("abba","dog cat cat dog"))
print(wordPattern("abba","dog cat cat fish"))
print(wordPattern("aaaa","dog cat cat dog"))
print(wordPattern("abba","dog dog dog dog"))

__author__ = 'JxKing'
# Given a string S, find the longest palindromic substring in S.
# You may assume that the maximum length of S is 1000,
#  and there exists one unique longest palindromic substring.
class Solution(object): # worst case,O(n3)
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        if len(s)<=1:
            return s
        letter_index={} #record letter's index
        for index in range(len(s)):
            letter=s[index]
            if letter not in letter_index:
                letter_index[letter]=[]
            letter_index[letter].append(index)
        length_index={} # mapping distance with indexes
        length=set()
        for letter in letter_index:
            if len(letter_index[letter])>0:
                for i in letter_index[letter]:
                    for j in letter_index[letter]:
                        if i!=j:
                            if abs(i-j) not in length_index:
                                length_index[abs(i-j)]=[]
                            length_index[abs(i-j)].append([i,j])
                            length.add(abs(i-j))
        length=list(length)
        length.sort(reverse=True)
        for l in length:
            for index in length_index[l]:
                index1,index2=min(index[0],index[1]),max(index[0],index[1])
                if self.checkPalindrome(s[index1:index2+1]):
                    return s[index1:index2+1]
        return ''
    def checkPalindrome(self,s):
        if len(s)<=1:return True
        if len(s)==2:
            if  s[0]==s[1]:return True
            else:return False
        if s[0]==s[-1]:
            return self.checkPalindrome(s[1:-1])
        else:return False


class Solution(object): # worst case,O(n2)
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        l=len(s)
        if l<=1:return s
        if l==2:
            if s[0]==s[-1]:return s
            else:return s[0]
        best=''
        for i in range(0,l-1): #let the pivot position starts from i
            if i==0: left=''
            else:left+=s[i-1]
            j=i
            while j<=l-2 and s[j+1]==s[j]: # determine which position the pivot ends
                j+=1
            mid=s[i:j+1] #the pivot
            right=s[j+1:]
            current=self.checkPalindrome(left,right,mid) #current best
            if len(current)>len(best):
                best=current
        return best


    def checkPalindrome(self,left,right,mid):
        cnt=0
        minl=min(len(left),len(right))
        if minl==0:
            return mid
        while cnt<minl and left[-(cnt+1)]==right[cnt]: #looking for the max index that can be combined with the mid
            cnt+=1
        if cnt==0:
            return mid
        return left[-(cnt):]+mid+right[:cnt]

solution=Solution()
print(solution.longestPalindrome('232123454321'))
print(solution.longestPalindrome('1'))
print(solution.longestPalindrome("gphyvqruxjmwhonjjrgumxjhfyupajxbjgthzdvrdqmdouuukeaxhjumkmmhdglqrrohydrmbvtuwstgkobyzjjtdtjroqpyusfsbjlusekghtfbdctvgmqzeybnwzlhdnhwzptgkzmujfldoiejmvxnorvbiubfflygrkedyirienybosqzrkbpcfidvkkafftgzwrcitqizelhfsruwmtrgaocjcyxdkovtdennrkmxwpdsxpxuarhgusizmwakrmhdwcgvfljhzcskclgrvvbrkesojyhofwqiwhiupujmkcvlywjtmbncurxxmpdskupyvvweuhbsnanzfioirecfxvmgcpwrpmbhmkdtckhvbxnsbcifhqwjjczfokovpqyjmbywtpaqcfjowxnmtirdsfeujyogbzjnjcmqyzciwjqxxgrxblvqbutqittroqadqlsdzihngpfpjovbkpeveidjpfjktavvwurqrgqdomiibfgqxwybcyovysydxyyymmiuwovnevzsjisdwgkcbsookbarezbhnwyqthcvzyodbcwjptvigcphawzxouixhbpezzirbhvomqhxkfdbokblqmrhhioyqubpyqhjrnwhjxsrodtblqxkhezubprqftrqcyrzwywqrgockioqdmzuqjkpmsyohtlcnesbgzqhkalwixfcgyeqdzhnnlzawrdgskurcxfbekbspupbduxqxjeczpmdvssikbivjhinaopbabrmvscthvoqqbkgekcgyrelxkwoawpbrcbszelnxlyikbulgmlwyffurimlfxurjsbzgddxbgqpcdsuutfiivjbyqzhprdqhahpgenjkbiukurvdwapuewrbehczrtswubthodv"))
print(solution.longestPalindrome('112211'))
print(solution.longestPalindrome('aaabaaaa'))
print(solution.longestPalindrome('121'))
print(solution.longestPalindrome("eeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeee"))
print(solution.longestPalindrome("1111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111"))
print(solution.longestPalindrome('abb'))
print(solution.longestPalindrome('ccc'))
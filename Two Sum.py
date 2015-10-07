__author__ = 'JxKing'
# Given an array of integers, find two numbers such that they add up to a specific target number.
#
# The function twoSum should return indices of the two numbers such
# that they add up to the target, where index1 must be less than index2.
# Please note that your returned answers (both index1 and index2) are not zero-based.
#
# You may assume that each input would have exactly one solution.
#
# Input: numbers={2, 7, 11, 15}, target=9
# Output: index1=1, index2=2
def twoSum(nums, target):
    """
    :type nums: List[int]
    :type target: int
    :rtype: List[int]
    """
    num_index={}
    index=1
    for num in nums:
        if num not in num_index:
            num_index[num]=[]
        num_index[num].append(index)
        index+=1
    for num in nums:
        if target-num in num_index and target-num!=num:
            return num_index[num][0],num_index[target-num][0]
        if target-num in num_index and target-num==num:
            if len(num_index[num])>1:
                return num_index[num][0],num_index[num][1]

print(twoSum([2, 7, 11, 15],9))
print(twoSum([0, 4, 3, 0],0))
print(twoSum([3, 2, 4, 0],6))
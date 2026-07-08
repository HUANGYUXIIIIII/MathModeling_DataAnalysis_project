#leetcode-1512-好数对的数目
#哈希表公式法
如果一个数字共出现k次，那么组合数量就是k*（k-1）/2


暴力解题法
双层循环
外循环i从0到数组末尾
内循环j从i+1到末尾
如果两个元素相等，就+1
count = 0
n =len(nums)
for i in range (n):
	for j in range (i+1，n):
		if nums[i] == nums[j]:
				count += 1
return count				


class Solution(object):
    def numIdenticalPairs(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        from collections import Counter
        cnt = Counter(nums)
        res = 0
        for k in cnt.values():
            res += k*(k-1)//2
        return res
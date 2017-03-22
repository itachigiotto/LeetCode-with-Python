class Solution(object):
	def findMaxConsecutiveOnes(self, nums):
		index = [0]
		cut = 0
		for i in range(len(nums)):
			if nums[i]:
				index.append(index[i]+1)
			else:
				index.append(0)
		return max(index)

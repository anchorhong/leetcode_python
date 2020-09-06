

class Solution:
    def canJump(self, nums):
        dest = 1 + nums[0]
        for idx in range(1, len(nums)):
            if dest - 1 >= idx and dest < nums[idx] + idx + 1:
                dest = nums[idx] + idx + 1
        return True if dest >= len(nums) else False


if __name__ == '__main__':
    inputs = [3,2,1,0,4]
    print(Solution().canJump(inputs))

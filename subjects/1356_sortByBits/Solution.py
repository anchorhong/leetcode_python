from typing import List


class Solution:
    def sortByBits(self, arr: List[int]) -> List[int]:
        def numbers_of_bits(num: int) -> int:
            nums = 0
            while num != 0:
                if num & 1 == 1:
                    nums += 1
                num = num >> 1
            return nums

        arr.sort(key=lambda x: (numbers_of_bits(x), x))
        return arr


if __name__ == "__main__":
    arr = [0, 1, 2, 3, 4, 5, 6, 7, 8]
    arr = [1024,512,256,128,64,32,16,8,4,2,1]
    # arr = [1024,512,256,128,64,32,16,8,4,2,1]
    print(Solution().sortByBits(arr))

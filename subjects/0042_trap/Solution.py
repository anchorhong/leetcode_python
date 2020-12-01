from typing import List


class Solution:
    def trap(self, height: List[int]) -> int:
        n = len(height)
        has_decrease, need_decrease = False, True
        slow, fast = 0, 0
        total = 0
        while fast < n - 1:
            if need_decrease and not has_decrease and height[fast] <= height[fast + 1]:
                fast += 1
                slow = fast
            elif need_decrease and not has_decrease and height[fast] > height[fast + 1]:
                has_decrease = True
                fast += 1
            elif need_decrease and has_decrease and height[fast] >= height[fast + 1]:
                has_decrease = True
                fast += 1
            elif need_decrease and has_decrease and height[fast] < height[fast + 1]:
                need_decrease = False
                has_decrease = True
                fast += 1
            elif not need_decrease and height[fast] <= height[fast + 1]:
                fast += 1
            elif not need_decrease and height[fast] > height[fast + 1]:
                h = min(height[slow], height[fast])
                length = fast - slow - 1
                total += h * length - sum(height[slow + 1:fast])
                need_decrease = True
                has_decrease = False
                slow = fast
                fast += 1

        return total


if __name__ == "__main__":
    # height = [0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]
    height = [4, 2, 0, 3, 2, 5]
    print(Solution().trap(height))

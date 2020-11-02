from typing import List


class Solution:
    def videoStitching(self, clips: List[List[int]], T: int) -> int:
        if not clips:
            return -1
        clips.sort(key=lambda x: x[0])
        cur_flag, pre_end, flags = None, 0, 0
        for clip in clips:
            if cur_flag is None:
                if clip[0] > pre_end:
                    return - 1
                cur_flag = clip
                flags += 1
            else:
                if clip[0] <= pre_end and clip[1] > cur_flag[1]:
                    cur_flag = clip
                elif clip[0] > pre_end and clip[0] <= cur_flag[1]:
                    pre_end = cur_flag[1]
                    cur_flag = clip
                    flags += 1
                else:
                    continue
            if clip[1] >= T:
                return flags
        return -1


if __name__ == "__main__":
    clips = [[0, 2], [4, 6], [8, 10], [1, 9], [1, 5], [5, 9]]
    T = 10
    print(Solution().videoStitching(clips, T))

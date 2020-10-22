class Solution:
    def backspaceCompare(self, S: str, T: str) -> bool:
        i, j, s_back, t_back = len(S) - 1, len(T) - 1, 0, 0
        while i >= 0 and j >= 0:
            if s_back == 0 and t_back == 0 and S[i] != "#" and T[j] != "#" and \
                    S[i] != T[j]:
                return False
            elif S[i] == "#" and T[j] == "#":
                i, j, s_back, t_back = i - 1, j - 1, s_back + 1, t_back + 1
            elif S[i] == "#":
                i, s_back = i - 1, s_back + 1
            elif T[j] == "#":
                j, t_back = j - 1, t_back + 1
            elif s_back != 0:
                i, s_back = i - 1, s_back - 1
            elif t_back != 0:
                j, t_back = j - 1, t_back - 1
            elif S[i] == T[j]:
                i, j = i - 1, j - 1
        k = i if i >= 0 else j
        k_back = s_back if i >= 0 else t_back
        K = S if i >= 0 else T
        for k in range(k, -1, -1):
            if k_back == 0 and K[k] != "#":
                return False
            else:
                k_back = k_back + 1 if K[k] == "#" else k_back - 1
        return True


if __name__ == "__main__":
    S = "ab#c"
    T = "ad#c"
    print(Solution().backspaceCompare(S, T))
    S = "ab##"
    T = "c#d#"
    print(Solution().backspaceCompare(S, T))
    S = "a##c"
    T = "#a#c"
    print(Solution().backspaceCompare(S, T))
    S = "a#c"
    T = "b"
    print(Solution().backspaceCompare(S, T))
    S = "bcc##"
    T = "bc#c#"
    print(Solution().backspaceCompare(S, T))

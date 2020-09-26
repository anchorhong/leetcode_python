class Solution:
    def isOneBitCharacter(self, bits):
        if len(bits) < 2:
            return True
        return self.is_valid(bits[0:-1])

    def is_valid(self, bits):
        if len(bits) == 0:
            return True
        elif len(bits) == 1 and bits[0] == 1:
            return False
        elif bits[-1] == 1:
            return bits[-2] == 1 and self.is_valid(bits[:-2])
        else:
            if self.is_valid(bits[:-1]):
                return True
            return bits[-2] == 1 and self.is_valid(bits[:-2])


if __name__ == '__main__':
    bits = [1, 0, 0]
    bits1 = [1, 1, 1, 0]
    print(Solution().isOneBitCharacter(bits))
    print(Solution().isOneBitCharacter(bits1))

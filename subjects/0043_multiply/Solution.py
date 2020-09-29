class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        if num1 == "0" or num2 == "0":
            return "0"

        def translate(num_str: str) -> int:
            num = None
            for s in num_str:
                if not num:
                    num = int(s)
                else:
                    num = num * 10 + int(s)
            return num

        multiple = translate(num1) * translate(num2)
        return str(multiple)

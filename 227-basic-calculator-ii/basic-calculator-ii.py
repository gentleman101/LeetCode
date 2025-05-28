class Solution:
    def calculate(self, s: str) -> int:
        prev_op = '+'
        res = 0
        prev_num = 0
        cur_num = 0

        for i, char in enumerate(s):
            if char.isdigit():
                cur_num = cur_num * 10 + int(char)
            
            if not char.isdigit() and char != ' ' or i == len(s) - 1:
                if prev_op == '+':
                    res += prev_num
                    prev_num = cur_num
                elif prev_op == '-':
                    res += prev_num
                    prev_num = -cur_num
                elif prev_op == '*':
                    prev_num = prev_num * cur_num
                elif prev_op == '/':
                    # Integer division that truncates toward zero
                    prev_num = int(prev_num / cur_num)

                prev_op = char
                cur_num = 0

        res += prev_num
        return (res)
        
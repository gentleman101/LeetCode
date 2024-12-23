class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        for token in tokens:
            if token in {'+', '-', '*', '/'}:  # Set for better lookup
                # Pop the top two elements
                b = stack.pop()  # Second operand
                a = stack.pop()  # First operand
                
                # Perform the operation
                if token == '+':
                    stack.append(a + b)
                elif token == '-':
                    stack.append(a - b)
                elif token == '*':
                    stack.append(a * b)
                elif token == '/':
                    # Ensure integer division truncating toward zero
                    stack.append(int(a / b))
            else:
                # Push the number (convert string to integer)
                stack.append(int(token))
        
        # The result will be the only element in the stack
        return stack[0]

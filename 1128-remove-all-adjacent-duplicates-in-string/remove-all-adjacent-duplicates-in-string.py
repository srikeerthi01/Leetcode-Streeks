class Solution:
    def removeDuplicates(self, s: str) -> str:
        stack = []
        for ch in s:
            if stack and stack[-1] == ch:  #stack[-1] used to check with the ch is eaqaul to the last inserted element , we used stack because the stack is previously empty
                stack.pop()
            else:
                stack.append(ch)
        return "".join(stack)
         
        
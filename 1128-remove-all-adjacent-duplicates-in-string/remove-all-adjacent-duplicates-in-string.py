class Solution(object):
    def removeDuplicates(self, s):
        stack = []
        for ch in s:
            if not stack:
                stack.append(ch)
            elif stack[-1] == ch:
                stack.pop()
            else:
                stack.append(ch)
        return "".join(stack)

        
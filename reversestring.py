class solution:
    def reverseString(self,s:list[str]):
        stack = []
        for c in s:
            stack.append(c)
        i = 0
        while stack:
            s[i]=stack.pop()
            i=i+1




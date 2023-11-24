class Solution:
    def simplifyPath(self, path: str) -> str:
        path = [p for p in path.split('/') if p]
        stack = []
        for dire in path:
            if dire == '..' and len(stack):
                stack.pop()
            elif dire != '..' and dire != '.':
                stack.append(dire)
        return '/' + '/'.join(stack)
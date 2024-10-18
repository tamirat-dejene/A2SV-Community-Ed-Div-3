class Solution:
    def interpret(self, command: str) -> str:
        goal = ''
        i = 0
        while i < len(command):
            if command[i] == 'G':
                goal += 'G'
                i += 1
            elif command[i] == '(':
                if i + 1 < len(command):
                    if command[i + 1] == ')':
                        goal += 'o'
                        i += 2
                    else:
                        goal += 'al'
                        i += 4
                else:
                    i += 1
        return goal

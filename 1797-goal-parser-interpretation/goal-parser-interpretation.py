class Solution(object):
    def interpret(self, command):
        i=0
        output=""
        while i < len(command):
            if command[i] == 'G':
                output += 'G'
                i+=1
            elif command[i] == '(':
                if command[i+1] == ')':
                    output += 'o'
                    i += 2    
                else:
                    output += 'al'
                    i+=4
        return output                                
        
        
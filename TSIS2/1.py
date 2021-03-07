class Solution:
    def defangIPaddr(self, address: str) -> str:
        totl=''
        for i in address:
            if i == '.':
                totl = totl + '[.]'
            else: 
                totl = totl + i
        return(totl)

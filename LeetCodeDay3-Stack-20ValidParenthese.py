C:/Users/ITWILL/anaconda3/python.exe c:/Users/ITWILL/Desktop/python_workspace/LeetCodeDay3-Stack-20ValidParenthese.py

def isValid(s):
    print("this is s",s)
    open = ["(", "{", "["]
    close = [")", "}", "]"]
    my_dict = dict(zip(close, open))
    s = list(s)
    for i in s:
        if i in close:
            if my_dict[i] == s[s.index(i)-1]:
                index = s.index(i)
                s.pop(index)
                s.pop(index-1)
                if len(s) == 0:
                    return True              
            else: 
                return False

string = r"{}[]()"
isValid(string)
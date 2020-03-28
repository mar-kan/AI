#Kanellaki Maria Anna - 1115201400060


class Stack():

    def __init__(self):
        self.data = []
        #self.count = 0                 

    def empty(self):
        return len(self.data) == 0

    def full(self):
        return 0

    def push(self, symbol):
        self.data.append(symbol)
        #self.count += 1

    def pop(self):
        #self.count -= 1
        return self.data.pop()


def pair(ch1, ch2):
    if ch1 == '(':  
        return ch2 == ')'
    if ch1 == '[':
        return ch2 == ']'
    if ch1 == '{':
        return ch2 == '}'


if __name__== "__main__":

    symbols = raw_input('Enter an expression:')
    st = Stack()

    for i in symbols:
        if i == '(' or i == '{' or i == '[': 
            st.push(i)

        elif i == ')' or i == '}' or i == ']': 
            if not st.empty():
                if not pair(st.pop(), i):
                    print ('Characters not well balanced.\n')
                    exit(0)
            else:
                print ('Characters not well balanced.\n')
                exit(0)   
    
    if st.empty():
        print ('Characters well balanced.\n')
    else:
        print ('Characters not well balanced.\n')
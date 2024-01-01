class stack:
    def __init__(self,limit):
        self.stack=[]
        self.limit=limit
    def peek(self):
        if (len(self.stack))<=0:
            return -1
        else:
          print(self.stack[len(self.stack)-1])
    def pop(self):
        if (len(self.stack))<=0:
            return False
        else:
            return self.stack.pop()
    def push (self,data):
        if (len(self.stack))>=self.limit:
            return False
        else:
            self.stack.append(data)
    def display(self):
        if (len(self.stack))<=0:
            return False
        else:
            for i in self.stack:
                print(i)
    def is_empty(self):
        if (len(self.stack))<=0:
            return True
        else : return False
    def reverse(lst):
        s = stack(100)
        for e in lst:
         s.push(e)
        for i in range(len(lst)):
         lst[i] = s.pop()
        return lst
    def rev_stacks(s):
        s1=stack(100)
        s2=stack(100)
        while not s.is_empty():
            s1.push(s.pop())
        while not s1.is_empty():
            s2.push(s1.pop())
        while not s2.is_empty():
            s.push(s2.pop())
    def postfix(lst):
        s=stack((len(lst))//2)
        for e in lst:
            if e =="*":
             t2=s.pop()
             t1=s.pop()
             t=t1*t2
             s.push(t)
            elif e =="/":
             t2=s.pop()
             t1=s.pop()
             t=t1/t2
             s.push(t)
            elif e =="-":
             t2=s.pop()
             t1=s.pop()
             t=t1-t2
             s.push(t)
            elif e=="+":
             t2=s.pop()
             t1=s.pop()
             t=t1+t2
             s.push(t)
            else:
                s.push(e)
                return s.stack[0]
        def match_s(str):
            s=stack()
            for i in str:
                if i in "([{":
                    s.push(i)
                elif i in ")]}":
                    if s.peek()==i:
                        s.pop()
                    else:
                        return False
            if s.is_empty():
                return True
            else:
                return False

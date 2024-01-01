class graph:
    def __init__(self,n):
        self.size=n
        self.m=[]
        for i in range(n):
            self.m.append([0 for j in range(n)])
            
    def add_edge(self,v1,v2):
        self.m[v1][v2]=1
        self.m[v2][v1]=1
    def display(self):
        for h in range(self.size):
            for k in range(self.size):
                print("%d\t"%self.m[h][k],end="")
            print()
g=graph(4)
g.add_edge(0,1)
g.add_edge(0,2)
g.add_edge(1,2)
g.add_edge(2,3)
g.display()
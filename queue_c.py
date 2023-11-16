class queue_c:
  def init(self,k):
    self.k=k 
    self.queue=[None]*k
    self.front=-1
    self.rear=-1
    def insqueue(self,data):
      if self.rear%k==self.front:
        print("full")
      elif self.front==-1:
         self.front=0
         self.rear=0
         self.queue[self.rear]=data
      else:
        self.rear+=1
        self.queue[self.rear]=data
    def deletec(self):
     if self.front==-1:
         print("empty")
     elif self.front==self.rear:
         t=self.queue[self.front]
         self.front=-1
         self.raer=-1
         return t
     else:
         t=self.queue[self.front]
         self.fornt+=1
         return t
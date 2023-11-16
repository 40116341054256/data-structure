class queue:
  def __init__ (self,k):
    self.k=k 
    self.queue=[None]*k
    self.front=-1
    self.rear=-1
    def disqueue(self):
        if self.fornt==-1:
            print("empty")
        for i in range(self.fornt,self.rear+1):

            print(self.queue[i])
    def insqueue(self,data):
       if self.rear==-1:
          self.front=0
          self.rear=0
          self.queue[0]=data
       elif self.rear +1 == self.k:
          print("is full")
       else:
          self.queue[self.rear]=data
          self.rear+=1
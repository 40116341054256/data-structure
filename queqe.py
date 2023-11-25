# class queue:
#   def __init__ (self,k):
#     self.k=k 
#     self.queue=[None]*k
#     self.front=-1
#     self.rear=-1
#     def disqueue(self):
#         if self.fornt==-1:
#             print("empty")
#         for i in range(self.fornt,self.rear+1):

#             print(self.queue[i])
#     def insqueue(self,data):
#        if self.rear==-1:
#           self.front=0
#           self.rear=0
#           self.queue[0]=data
#        elif self.rear +1 == self.k:
#           print("is full")
#        else:
#           self.queue[self.rear]=data
#           self.rear+=1
     
class Queue:
    def __init__(self, k):
        self.k = k
        self.queue = [None] * k
        self.front = -1
        self.rear = -1

    def display(self):
        if self.front == -1:
            print("Empty")
        else:
            for i in range(self.front, self.rear + 1):
                print(self.queue[i], end=" ")
            print()

    def enqueue(self, data):
        if self.rear == self.k - 1:
            print("Queue is full")
        else:
            if self.front == -1:
                self.front = 0
            self.rear += 1
            self.queue[self.rear] = data

    def dequeue(self):
        if self.front == -1:
            print("Queue is empty")
        else:
            data = self.queue[self.front]
            if self.front == self.rear:
                self.front = -1
                self.rear = -1
            else:
                self.front += 1
            return data

    def enqueue_at_front(self, data):
        if self.front == 0:
            print("Cannot enqueue at front, queue is full")
        else:
            self.front -= 1
            self.queue[self.front] = data

    def enqueue_at_middle(self, data):
        if self.rear == self.k - 1:
            print("Cannot enqueue at middle, queue is full")
        else:
            middle = (self.front + self.rear) // 2
            self.rear += 1
            for i in range(self.rear, middle, -1):
                self.queue[i] = self.queue[i - 1]
            self.queue[middle] = data

    def dequeue_at_front(self):
        if self.front == -1:
            print("Queue is empty")
        else:
            data = self.queue[self.front]
            if self.front == self.rear:
                self.front = -1
                self.rear = -1
            else:
                self.front += 1
            return data

    def dequeue_at_middle(self):
        if self.front == -1:
            print("Queue is empty")
        else:
            middle = (self.front + self.rear) // 2
            data = self.queue[middle]
            for i in range(middle, self.rear):
                self.queue[i] = self.queue[i + 1]
            self.rear -= 1
            return data

    def dequeue_at_rear(self):
        if self.front == -1:
            print("Queue is empty")
        else:
            data = self.queue[self.rear]
            if self.front == self.rear:
                self.front = -1
                self.rear = -1
            else:
                self.rear -= 1
            return data


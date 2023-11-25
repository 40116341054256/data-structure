# class queue_c:
#   def init(self,k):
#     self.k=k 
#     self.queue=[None]*k
#     self.front=-1
#     self.rear=-1
#     def insqueue(self,data):
#       if self.rear%k==self.front:
#         print("full")
#       elif self.front==-1:
#          self.front=0
#          self.rear=0
#          self.queue[self.rear]=data
#       else:
#         self.rear+=1
#         self.queue[self.rear]=data
#     def deletec(self):
#      if self.front==-1:
#          print("empty")
#      elif self.front==self.rear:
#          t=self.queue[self.front]
#          self.front=-1
#          self.raer=-1
#          return t
#      else:
#          t=self.queue[self.front]
#          self.fornt+=1
#          return t
class CircularQueue:
    def __init__(self, k):
        self.k = k
        self.queue = [None] * k
        self.front = -1
        self.rear = -1

    def display(self):
        if self.front == -1:
            print("Queue is empty")
        else:
            if self.front <= self.rear:
                for i in range(self.front, self.rear + 1):
                    print(self.queue[i], end=" ")
            else:
                for i in range(self.front, self.k):
                    print(self.queue[i], end=" ")
                for i in range(0, self.rear + 1):
                    print(self.queue[i], end=" ")
            print()

    def enqueue(self, data):
        if (self.rear + 1) % self.k == self.front:
            print("Queue is full")
        else:
            if self.front == -1:
                self.front = 0
            self.rear = (self.rear + 1) % self.k
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
                self.front = (self.front + 1) % self.k
            return data

    def enqueue_at_front(self, data):
        if (self.rear + 1) % self.k == self.front:
            print("Cannot enqueue at front, queue is full")
        else:
            self.front = (self.front - 1 + self.k) % self.k
            self.queue[self.front] = data

    def enqueue_at_middle(self, data):
        if (self.rear + 1) % self.k == self.front:
            print("Cannot enqueue at middle, queue is full")
        else:
            middle = (self.front + self.rear) // 2
            self.rear = (self.rear + 1) % self.k
            if self.front <= self.rear:
                for i in range(self.rear, middle, -1):
                    self.queue[i] = self.queue[i - 1]
            else:
                for i in range(self.rear, middle, -1):
                    self.queue[i] = self.queue[(i - 1 + self.k) % self.k]
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
                self.front = (self.front + 1) % self.k
            return data

    def dequeue_at_middle(self):
        if self.front == -1:
            print("Queue is empty")
        else:
            middle = (self.front + self.rear) // 2
            data = self.queue[middle]
            if self.front <= self.rear:
                for i in range(middle, self.rear):
                    self.queue[i] = self.queue[i + 1]
            else:
                for i in range(middle, self.rear):
                    self.queue[i] = self.queue[(i + 1) % self.k]
                self.rear = (self.rear - 1 + self.k) % self.k
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
                self.rear = (self.rear - 1 + self.k) % self.k
            return data

# Example usage:
my_circular_queue = CircularQueue(5)
my_circular_queue.enqueue(1)
my_circular_queue.enqueue(2)
my_circular_queue.enqueue(3)
my_circular_queue.enqueue(4)
my_circular_queue.enqueue(5)
my_circular_queue.display()
my_circular_queue.enqueue_at_front(0)
my_circular_queue.display()
my_circular_queue.enqueue_at_middle(100)
my_circular_queue.display()
my_circular_queue.dequeue_at_rear()
my_circular_queue.display()

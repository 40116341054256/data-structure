class btnode():
    def __init__(self,data,left=None,right=None):
        self.data=data
        self.left=left
        self.right=right
class tree():
    def __init__(self,root=None):
        self.root = root
    def inorder (self,root):
        if self.root is None:
            return
        else:
            self.inorder(root.left)
            print(root.data)
            self.inorder(root.right)
    def postorder(self,root):
         if self.root is None:
            return
         else:
             self.postorder(root.left)
             self.postorder(root.right)
             print(root.data)
    def preorder(self,root):
        if self.root is None:
            return
        else:
            print(root.data)
            self.preorder(root.left)
            self.preorder(root.right)
class nodebst():
     def __init__(self,data):
        self.key=data
        self.left=None
        self.right=None

     def searchBst(self,k):
        if self is None or self.key == k:
            return self
        elif k < self.key:
            return self.left.searchBst(k) if self.left else None
        else:
            return self.right.searchBst(k) if self.right else None
     def insertBst(self,root, k):
        if root is None:
            return nodebst(k)
        if k<root.key:
           root.left=self.insertBst(root.left,k)
        else:
            root.right = self.insertBst(root.right,k)
        return root
     def minvalueBst(root):
        if root is None:
            return root
        while (root.left is not None):
            root=root.left
        return root.key
     def minWithRE(self):
        if self.left is None:
            return self
        else:
            return self.left.minWithRE()
     def heapify(self,a, k):
      left = 2 * k + 1
      right = 2 * k + 2
      s = k

      if left < len(a) and a[left] < a[s]:
        s = left
      if right < len(a) and a[right] < a[s]:
        s = right

      if s != k:
        a[k], a[s] = a[s], a[k]
        self.heapify(a,s)

     def min_heap(self,a):
      n=int((len(a)//2)-1)
      for i in range(n,-1,-1):
       self.heapify(a,i)
     def heap_sort(a,min_heap,heapify):
          n = len(a)
          for i in range(n//2 - 1, -1, -1):
           min_heap(a, n, i)
          for i in range(n-1, 0, -1):
           a[i], a[0] = a[0], a[i]
          heapify(a, i, 0)

class MaxHeap:
      def __init__(self):
        self.heap = []

      def parent(self, i):
        return (i - 1) // 2

      def left(self, i):
        return 2 * i + 1

      def right(self, i):
        return 2 * i + 2

      def size(self):
        return len(self.heap)

      def is_empty(self):
        return self.size() == 0

      def build_max_heap(self, array):
        self.heap = array
        for i in range((len(array) - 2) // 2, -1, -1):
            self.max_heapify(i)

      def max_heapify(self, i):
        largest = i
        l = self.left(i)
        r = self.right(i)

        if l < self.size() and self.heap[l] > self.heap[largest]:
            largest = l

        if r < self.size() and self.heap[r] > self.heap[largest]:
            largest = r

        if largest != i:
            self.heap[i], self.heap[largest] = self.heap[largest], self.heap[i]
            self.max_heapify(largest)

      def extract_max(self):
        if self.is_empty():
            return "Heap is empty"

        max = self.heap[0]
        self.heap[0] = self.heap.pop()
        self.max_heapify(0)
        return max
      
      def build_max_heap(self,arr, n, i):
       largest = i
       left = 2 * i + 1
       right = 2 * i + 2

       if left < n and arr[i] < arr[left]:
        largest = left
       if right < n and arr[largest] < arr[right]:
        largest = right
       if largest != i:
         arr[i], arr[largest] = arr[largest], arr[i]
         self.build_max_heap(arr, n, largest)

      def heapify_max(self,arr, n, i):
          largest = i
          left = 2 * i + 1
          right = 2 * i + 2

          if left < n and arr[i] < arr[left]:
            largest = left
          if right < n and arr[largest] < arr[right]:
            largest = right
          if largest != i:
           arr[i], arr[largest] = arr[largest], arr[i]
           self.heapify_max(arr, n, largest)

      def heap_sort(arr,build_max_heap,heapify_max):
         n = len(arr)
         for i in range(n//2 - 1, -1, -1):
          build_max_heap(arr, n, i)
         for i in range(n-1, 0, -1):
          arr[i], arr[0] = arr[0], arr[i]
          heapify_max(arr, i, 0)

      def insert(self,arr, new):
             arr.append(new)
             i = len(arr) - 1
             self.heapify_max(arr, i + 1, i)
a=[5,6,3,1,4,2,7]
s=nodebst(5)
s.min_heap(a)
print(a)
s.left=nodebst(3)
s.left.left=nodebst(2)
s.left.right=nodebst(4)
s.right=nodebst(8)
s.right.left=nodebst(7)
s.searchBst(8)
s.insertBst(s,15)
s.searchBst(14)
s.min_heap(a)
s.heapify(a,5)
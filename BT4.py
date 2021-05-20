class Node:
    def __init__(self, x=None):
        self.data = x
        self.next = None
class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def insertTail(self, x): # add vi tri cuoi cung
        p = Node(x)
        if (self.head == None):
            self.head = p
            self.tail = p
        else:
            self.tail.next = p
            self.tail = p

    def push(self,x): #add vi tri dau tien
        p = Node(x)
        p.next= self.head
        self.head = p

    def addphantu(self, n, pos): # add phan tu 2 ,3,4, .....
        cur= self.head
        p= Node(n)
        i=0
        while (i < pos-1) and cur != None:
            i+=1
            cur =cur.next
        p.next= cur.next
        cur.next=p

    def demsoluongnode(self):
        count = 0
        cur = self.head
        if(self.head==None):
            return None
        while(cur != None):
            count = count+1
            cur=cur.next
        return count
    def print(self):
        cur=self.head
        while(cur):
            print(cur.data ,"",  end="")
            cur=cur.next
ll = LinkedList()
while (1 < 7):
    n = int(input())
    if n == 0:
        break
    ll.insertTail(n)
pos = ll.demsoluongnode() # dem so luong node de xac dinh vi tri
m=1
for i in range(1,2*pos-1,2):
    m = m + 1
    ll.addphantu(m, i)
ll.push(1)
ll.print()

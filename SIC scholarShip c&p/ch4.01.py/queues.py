class Queues:
    def __init__ (self):
        self.queue=[]
    def __str__(self):
        return str(self.queue)
    def isEmpty(self):
        return  self.queue == []
    def enqueue(self,item):
        self.queue.append(item)
    def dequeue(self):
        return self.queue.pop(0)
    def peek(self):
        return self.queue[0]
    def size(self):
        return len(self.queue)

def jousef_sequense(n,k):
    myq = Queues()
    for i in  range(1, n+1):
        myq.enqueue(i)

    while myq.size() >1: #then the loop would enter otherwise the player wins
        for i in range (k):
            myq.enqueue(myq.dequeue())
        myq.dequeue()

    return myq.peek()

print(jousef_sequense(4,2))








# # Create a queue
# # First In First Out
# myQueue = Queues()
# print('ice cream line')
# myQueue.enqueue("Mama")
# myQueue.enqueue("Baba")
# myQueue.enqueue("Zozy")
# print(myQueue)
#
# lenss = myQueue.size()
# for i in range(lenss):
#     myQueue.dequeue()
#     print("custmor is served\n","customers left : ",myQueue)

# myQueue = Queues()
# myQueue.enqueue("Mama")
# myQueue.enqueue("Baba")
# myQueue.enqueue("Zozy")
#
# if not myQueue.isEmpty():
#     print(myQueue.peak(), "is finished")
#     myQueue.dequeue()







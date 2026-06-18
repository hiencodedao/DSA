from revisedPriorityQueue import *

def identity(x): return x

queue = PrioritizeQueue(size=10, pri=identity) 

for i in range(5): 
    queue.insert(i) 

queue.remove()

print(queue)
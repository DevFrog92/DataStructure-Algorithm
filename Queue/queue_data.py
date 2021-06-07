import queue

data = queue.Queue()

# Enqueue
data.put('data1')
data.put('data2')

# Q의 크기를 알 수 있다.
print("Queue 크기",data.qsize())

# Dequeue - FIFO
print("FIFO 방식",data.get())
print("FIFO 방식",data.get())
print("-"*30)

### LIFO 큐 이용하기

data_LIFO = queue.LifoQueue()
data_LIFO.put('data1')
data_LIFO.put('data2')

print("LIFO 방식",data_LIFO.get())
print("LIFO 방식",data_LIFO.get())
print("-"*30)

### Priority Queue

data_Priority = queue.PriorityQueue()
data_Priority.put((3,'data3'))
data_Priority.put((1,'data1'))
data_Priority.put((2,'data2'))

print("우선순위 큐",data_Priority.get())
print("우선순위 큐",data_Priority.get())
print("우선순위 큐",data_Priority.get())
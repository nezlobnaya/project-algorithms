class Stack:
  def __init__(self):
    self.storage = []

  def push(self, item):
    self.storage.append(item)

  def pop(self):
    return self.storage.pop();

  def peek(self):
    return self.storage[-1];

  def isEmpty(self):
    return len(self.storage) == 0
  
  def printContents(self):
    for item in self.storage:
      print(item)

def sortStack(stack: Stack) -> Stack:
  aux = Stack()
  while not stack.isEmpty():
    temp =stack.pop()
    while not aux.isEmpty() and aux.peek() < temp:
      stack.push(aux.pop())
    aux.push(temp)
  
  while not aux.isEmpty():
    stack.push(aux.pop())
  return stack

s = Stack()
s.push(4)
s.push(10)
s.push(8)
s.push(5)
s.push(1)
s.push(6)

s.printContents()

print("_________________")
sortedStack = sortStack(s) # sortedStack is also a Stack instance

sortStack(s).printContents()

# def sortStack(stack: Stack) -> Stack:
#   output = Stack()
#   shouldContinue = True
#   while shouldContinue:
#     shouldContinue = False
#     m = 0
#     while not stack.isEmpty():
#       temp = stack.pop()
#       #print(temp)
#       if temp > m:
#         if m != 0:
#           output.push(m)
#         m = temp
#       else:
#         output.push(temp)
#         shouldContinue = True
#     stack.push(m)
#     while not output.isEmpty():
#       stack.push(output.pop())
  
#   return stack
    
from DataStructs import *

stack = Stack(10)
for word in ["I ", "like", "cheese", "cheese", "is" , "good"]:
    stack.push(word)
print("The length of the Stack is", len(stack))

print("Checking Stack is ", len(stack), "in size")
print("Stack contains:")
print(stack)
print("Is the stack full:", stack.isFull())

print("poping from stack:")
while not stack.isEmpty():
    print("pop --> ", stack.pop())
print()

print("The length of the Stack is", len(stack))
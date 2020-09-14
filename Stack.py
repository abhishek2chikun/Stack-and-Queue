#Creating a Stack through array
#Creating stack function
def createstack():
    stack=[]
    return stack
def isEmpty(stack):
    return len(stack)==0
def push(stack,item):
    stack.append(item)
    print(item,"is pushed to you stack:",stack)
def pop(stack):
    if isEmpty(stack)==True:
        print("\nStack is empty,Under FLow")
    else:
        popped=stack.pop()
        print(popped,"is pop out from the stack",stack)
def peek(stack):
    if isEmpty(stack)==True:
        print("\nStack is empty,Under FLow")
    else:
        print("\npeek of stack is",stack[len(stack)-1])
S=createstack()
for i in range(1,10):
    push(S,i*10)
pop(S)
pop(S)
pop(S)
peek(S)
print(isEmpty(S))
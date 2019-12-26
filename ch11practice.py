import time
import sys

def arraysum(x):
    return(sum(x))

def deletearray(x,):
    while len(x) > 0 : x.pop()

name = input("Enter name: ") 
if name == 'q':
    sys.exit()
try:
    x = [int(i) for i in input().split()]
except ValueError:
    print("only numbers!")
    sys.exit()
elapsetime = 0
t1 = time.time()
ans = arraysum(x)
deletedarray = deletearray(x)
t2 = time.time()
elapsetime = (t2 - t1) * 1000
print("Name: ",name)
print("Sum: ",ans)
print("Array: ",deletedarray)
print("Time: ", elapsetime, "ms")




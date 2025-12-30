"""a=5
b=6
c=a+b
print(c)
#REPL-READ,EVAL,PRINT,LOOP:
#PFO-FUNCTIONAL,OBJECT ORIENTED,PROGRAMMABLE

def pm():
    print("hello")
pm()
"""
n=int(input())
for i in range(1,n+1):
    for j in range(1,i+1):
        print(i, end=" ")
    print()
    
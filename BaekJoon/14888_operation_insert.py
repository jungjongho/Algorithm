from itertools import permutations
import sys
input = sys.stdin.readline

N=int(input())
number=list(map(int,input().split()))
operation=list(map(int,input().split()))

op=['+', '-', '*', '/']



operation_list=[]

for i,op in zip(operation,op):
    for k in range(i):
        operation_list.append(op)



operation_array=list(set(permutations(operation_list,len(operation_list))))

operation_array = list(map(list, operation_array))

result=[]

def operation_f(number_section,operation):
    number_list=number_section.copy()
    if len(number_list)==1:
        result.append(number_list[0])
        return

    if operation[0]=='+':
        tmp=number_list[0]+number_list[1]
        number_list.remove(number_list[1])
        number_list.remove(number_list[0])
        number_list.insert(0,tmp)
        operation.remove(operation[0])


    elif operation[0]=='-':
        tmp=number_list[0]-number_list[1]
        number_list.remove(number_list[1])
        number_list.remove(number_list[0])
        number_list.insert(0,tmp)
        operation.remove(operation[0])


    elif operation[0]=='*':
        tmp=number_list[0]*number_list[1]
        number_list.remove(number_list[1])
        number_list.remove(number_list[0])
        number_list.insert(0,tmp)
        operation.remove(operation[0])


    elif operation[0]=='/':
        if number_list[0]<0:
            tmp=-(-number_list[0]//number_list[1])
        else:
            tmp=number_list[0]//number_list[1]
        number_list.remove(number_list[1])
        number_list.remove(number_list[0])
        number_list.insert(0,tmp)
        operation.remove(operation[0])
                
    operation_f(number_list,operation)



for i in operation_array:
    operation_f(number,i)
print(max(result))
print(min(result))





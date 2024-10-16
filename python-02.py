
one_lst = []
two_lst = []
result_lst = []

for x in range(10) :
    one_lst.append(int(input("L1 Insert a number here : ")))
    two_lst.append(int(input("L2 Insert a number here : ")))
    
for x in range(10) : 
    result_lst.append(one_lst[x] + two_lst[x])
    
print(result_lst)
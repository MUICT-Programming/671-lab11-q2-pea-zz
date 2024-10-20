# YOUR CODE HERE
n= int(input())
lst1=[]
lst2=[]

for i in range(n):
    lst1.append(int(input()))
#print(lst1)
for i in range(n):
    lst2.append(int(input()))
#print(lst2)
#print(lst1+lst2)

#use zip to + list
def summation(lst1,lst2):
    updated_list  = [a + b for a, b in zip(lst1, lst2)]
    return updated_list
def find_min_max(updated_list):
    return (min(updated_list),max(updated_list))

#Calculate the updated list using summation
updated_list = summation(lst1, lst2)
    
#Find min and max using find_min_max
min_max = find_min_max(updated_list)
   
print(updated_list)
print(min_max)

''' Maximum Sub Array using Diveidee and conquer. '''

def divide(array, l, r):
    if(l==r):
        return [l,l,array[l]];
    
    m = int((l+r)/2)
    list1 = divide(array, l, m)
    list2 = divide(array, m+1, r)
    list3= merge(array,l,m,r)

    if(list1[2] > list2[2]) and (list1[2] > list3[2]):
        largest = list1[2]
        return list1;
    elif(list2[2] > list1[2]) and (list2[2] > list3[2]):
        largest = list2[2]
        return list2;
    else:
        largest = list3[2]
        return list3;
        

def merge(array, l, m, r):
    global min_index
    global max_index

    sum_left = float("-inf")
    total = 0
    for i in range(m,l-1,-1):
        total +=array[i]
        if total > sum_left:
            sum_left = total
            min_index = i

    sum_right = float("-inf")
    total = 0
    for j in range(m+1, r+1):
        total +=array[j]
        if total > sum_right:
            sum_right = total
            max_index = j

    return [min_index, max_index, sum_left + sum_right];
        

array = [1,-4,3,-4]
min_index = 0
max_index = 0
list_final = divide(array,0,len(array)-1)

sum_all = 0
for p in range(len(array)):
    sum_all +=array[p]

if list_final[2] > sum_all:
   print('Min Index: ',list_final[0],' and Max Index: ',list_final[1],' and sum is',list_final[2])
elif sum_all > list_final[2]:
    print('Min Index: 0 and Max Index: ',(len(array)-1),' and sum is',sum_all)
elif sum_all == sum_divide:
    print('Min Index: ',list_final[0],' and Max Index: ',list_final[1],' and sum is',sum_divide," and also")
    print('Min Index: 0 and Max Index: ',(len(array)-1),' and sum is',sum_all)

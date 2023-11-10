#!/usr/bin/env python
# coding: utf-8

# In[28]:


#Find leader numbers
a = [16, 17, 4, 3, 5, 2]
leaders = []

for i in range(len(a)):
    if a[i] == max(a[i:]):
        leaders.append(a[i])

print("Leader numbers:", leaders)


# In[43]:


#
a = [4, 3, 7, 8, 6, 2, 1]

for i in range(len(a)-1):
    if (i % 2 == 0) == (a[i] > a[i+1]):
        a[i], a[i+1] = a[i+1], a[i]

print("Zigzag ordered array:", a)


# In[ ]:


for i in range(len(a)-1):
    if (i % 2 == 0) == (a[i] > a[i+1]):
        a[i], a[i+1] = a[i+1], a[i]


# In[6]:


#bubble sort
a = [5, 4, 3, 2, 1]
for i in range(len(a)-2):
    if (i % 1 == 0) == (a[i] < a[i+1]):
        a[i], a[i+1] = a[i+1], a[i]

print("Zigzag ordered array:", a)


# In[8]:


def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]

a = [5, 4, 3, 2, 7]
bubble_sort(a)
print("Sorted list:", a)


# In[14]:


def selection_sort(arr):
    for i in range(len(arr)):
        min_idx = i
        for j in range(i + 1, len(arr)):
            if arr[j] < arr[min_idx]:
                min_idx = j
        arr[i], arr[min_idx] = arr[min_idx], arr[i]
a = [5, 4, 3, 2, 1]
selection_sort(a)
print(a) 


# In[20]:


a = [1, 2, 3, 4, 5]
target_sum = 9
num_elements = 3
if a[0]+a[1]+


# In[31]:


a = [12, 3, 4, 1, 6, 9]
target_sum = 24

for combo in itertools.combinations(a, 3):
    if sum(combo) == target_sum:
        print(f"Found: {combo}")
        break
else:
    print("No combination found that sums up to 24.")


# In[3]:


a=[1,2,3,4,5]
n=len(a)
for i in range(n):
    j=i+1
    
for k in range(j+1):
    if (i+j+k)==9:
        print(i,j,k)


# In[23]:


a = [0, 0, 1, 2, 0, 1, 2, 2, 1]
a[0]=0
a[1]=0
a[2]=0
a[3]=1
a[4]=1
a[5]=1
a[6]=2
a[7]=2
a[8]=2
print(a)


# In[40]:


a = [0, 1, 2, 0, 1, 2, 0, 1, 2]
values = []
for i in a:
    if i==0:
        values.append(i)
        count=3
        if i + 1 in a:
            values.append(i + 1)

print(values)


# In[1]:


a=[0,1,2,0,1,2,0,1,2]
for i in a:
    if i==i:
        a.append(i)
        a.remove(i)
    for j in a:
        if j==i+1:
            a.append(j)
            a.remove(j)
            
print(a)


# In[5]:


a = [1, 10, 11, 12, 11, 1]
new_a = []
for i in a:
    if i not in new_a:
        new_a.append(i)
        
print(new_a)


# In[9]:


def mergeSort(arr):
    if len(arr) > 1:
        mid = len(arr)//2
        sub_array1 = arr[:mid]
        sub_array2 = arr[mid:]
        mergeSort(sub_array1)
        mergeSort(sub_array2)
        i = j = k = 0
        while i < len(sub_array1) and j < len(sub_array2):
            if sub_array1[i] < sub_array2[j]:
                arr[k] = sub_array1[i]
                i += 1
            else:
                arr[k] = sub_array2[j]
                j += 1
            k += 1
        while i < len(sub_array1):
            arr[k] = sub_array1[i]
            i += 1
            k += 1
        while j < len(sub_array2):
                arr[k] = sub_array2[j]
                j += 1
                k += 1
arr = [6,4,2,3,1,9,8,3,5]
mergeSort(arr)
print(arr)


# In[13]:


def merge_sort(arr):
    if len(arr) <= 1:
        return arr
    mid = len(arr) // 2
    left, right = arr[:mid], arr[mid:]
    return merge(merge_sort(left), merge_sort(right))

arr = [12, 11, 8, 5, 6, 7]
sorted_arr = merge_sort(arr)
print("Sorted array:", sorted_arr)


# In[5]:


a = [[7, 6, 5],
     [1, 2, 3],
     [8, 4, 9]]
for i in a:
    if i==i:
        a.append(i)
        a.remove(i)
    for i in a:
        if i==i:
            a.append(j)
            a.remove(j)
            
print(a)


# In[10]:


a = [[7, 6, 5],
     [1, 2, 3],
     [8, 4, 9]]

sorted_a = [sorted(row, reverse=True) for row in a]

for row in sorted_a:
    print(row)


# In[13]:


a = [[5, 6, 7],
     [1, 2, 3],
     [8, 4, 9]]

num_a = sorted([num for row in a for num in row])

sorted_a = [num_a[i:i+3] for i in range(0, len(num_a), 3)]

print(sorted_a)


# In[4]:


a = [[1, 2, 3],
     [4, 5, 6],
     [7, 8, 9]]

for i in range(min(len(a), len(a[0]))):
    a[i][i] = 0
    a[i][len(a)-i-1] = 0
 
for row in a:
    print(row)


# In[5]:



2+2+2


# In[6]:


-11-11-11-11-11


# In[7]:



num1 = 5
num2 = 3
result = multiply(num1, num2)
print(f"{num1} * {num2} = {result}")


# In[ ]:


def multiply(a, b):
    result = 0
    for _ in range(abs(b)):
        result += a if b > 0 else -a
    return result

a=int(input())
b=int(input())
result=multiply(a, b)
print(result)


# In[3]:


def min_curse(N, D, teachers):
    teachers.sort(key=lambda x: x[0])

    dp = [[float('inf')] * (D + 1) for _ in range(N + 1)]
    dp[0][0] = 0

    for i in range(1, N + 1):  
        arrival_day, lectures, curse = teachers[i - 1]
        for day in range(D + 1):
            dp[i][day] = min(dp[i][day], dp[i - 1][day])
    
            if day >= arrival_day:
                dp[i][day] = min(dp[i][day], dp[i - 1][day - arrival_day] + curse)

    min_curse_on_last_day = min(dp[N])

    return min_curse_on_last_day

N, D = map(int, input().split())
teachers = [list(map(int, input().split())) for _ in range(N)]

result = min_curse(N, D, teachers)
print(result)


# In[ ]:




















































































 


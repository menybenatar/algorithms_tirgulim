import winsound

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')
    freq = 500
    dur = 100
    winsound.Beep(freq, dur)
    # Press Ctrl+F8 to toggle the breakpoint.
# מציאת מקס מינ פתרון נאיבי
def find_min_max_A(arr,n):
    if arr[0] >= arr[1]:
        max = arr[0]
        min = arr[1]
    else:
        max = arr[1]
        min = arr[0]
    for i in range(2,n):
        if (arr[i] > max):
            max = arr[i]
        elif(arr[i] < min):
            min = arr[i]
    return (min ,max)


# פתרון ב 3/2 N כאשר N זוגי  נקבל : 3(n-2)/2 +1
# n even :
# 3((n-2)/2) +1 =
# n odd :
#3((n-2)/2) +4 =
def find_min_max_B(arr,n):
    if arr[0] >= arr[1]:
        max = arr[0]
        min = arr[1]
    else:
        max = arr[1]
        min = arr[0]
    for i in range(3,n,2):
        if (arr[i] > arr[i-1]):
            max_locl = arr[i]
            min_locl = arr[i-1]
        else:
            max_locl = arr[i-1]
            min_locl = arr[i]
        if(max_locl>max):
            max = max_locl
        if (min_locl < min ):
            min = min_locl
    if n%2:
        if (arr[n-1]>max):
            max = arr[n-1]
        if(arr[n-1]<min):
            min = arr[n-1]
    return (min ,max)

# שאלה 2 מתרגול 1 נתון מערך של בהתחלה מלא 1 ואחרכך מלא 0 צריך למצוא את המקום הראשון של האפס בסיבוכיות שונות
#O(n)
def find_the_t_A(arr,n):
    for i,j in zip(arr,range(n)):
        if(i == 0):
            return j
#log(n)
def find_the_t_B(arr, n):

    if(arr[0] == 0):
        return 0
    if (arr[n-1] == 1):
        return n

    low = 0
    high = n-1

    while low <= high:
        mid = int((low + high) / 2)
        if(arr[mid] == 0 and arr[mid-1] == 1):
            return mid
        if (arr[mid] == 1):
            low =mid +1
        elif(arr[mid] == 0):
            high = mid-1

#Olog(t)
def find_the_t_C(arr, n):
    low = 0
    if (arr[low] == 0):
        return 0
    low += 1
    if (arr[low] == 0):
        return low
    low*=2
    while(2*low < n and arr[2*low] != 0):
        low *= 2
        if (2*low<n):
            high = 2*low-1
        else:
            high =n-1

    while low <= high:
        mid = int((low + high) / 2)
        if (arr[mid] == 0 and arr[mid - 1] == 1):
            return mid
        if (arr[mid] == 1):
            low = mid + 1
        elif (arr[mid] == 0):
            high = mid - 1









# אלגורתים למציאת הכוכב  n^2
def find_the_star(graph, n):
    for i in range(n):
        flag = 1
        for j in range(n):
            if (i == j):
                continue
            if (graph[i][j] == 1 or graph[j][i] == 0):
                flag = 0
                break
        if (flag == 1):
            return chr(65+i)

    return -1

# אלגורתים למציאת הכוכב n
def find_the_star_fast(graph, n):
    vartesies = []
    for i in range(n):
        vartesies.append(i)

    size = n
    while(size > 1):
        if(graph[vartesies[0]][vartesies[1]] == 1):
            vartesies[0] = vartesies[size-1]
        else:
            vartesies[1] = vartesies[size - 1]
        size -= 1

    i = vartesies[0]

    for j in range(n):
        if (i == j):
            continue
        if (graph[i][j] == 1 or graph[j][i] == 0):
            return -1

    return chr(65+i)


#  עם פעולת קסור אלגוריתם למציאת האיבר החסר בתוך מערך בטווח ה N
def find_the_missing(arr,n):
    sum_range = 0
    for i in range(n):
        sum_range = sum_range ^ i
    sum_arr = 0

    for j in arr:
        sum_arr = sum_arr ^ j

    return sum_range ^ sum_arr
import math
def check_if_is_prime_num(n):
    if n < 2:
        return False
    flag = True
    if n == 2 :
        return flag
    if (n > 2):
        for i in range (2,int(math.sqrt(n))):
            if(n % i == 0):
                flag = False
                break
    return flag ,i

#בעיית הרוב
def find_the_mojority_element_in_arr(arr):
    counter = 0
    candidate = None
    for i in arr:
        if counter ==0 :
            candidate = i
        if i == candidate:
            counter +=1
        else :
            counter-=1
    num_in_arr =0
    for x in arr:
        if(x == candidate):
            num_in_arr+=1
    if(num_in_arr >= len(arr)//2):
        return candidate
    else:
        return None

def sum_of_prime_number_equal_to_k(k):
    my_arr=[]

    for num in range(3, k//2):
        prime = True
        for i in range(2, num):
            if (num % i == 0):
                prime = False
        if prime:
            my_arr.append(num)
    sum = 0; j = 0

    for x,i in zip(my_arr,range(0,len(my_arr))) :
        while(sum>k and sum+x>k and sum != k):
            sum = sum - my_arr[j]
            my_arr.remove(my_arr[j])
            i-=1
        if (sum < k):
            sum += x
        else:
            return my_arr[0:i]

# מערך עם N איברים למצאת את הזוג במערך שמופיע הכי הרבה פעמים סיבוכיות NLOGN
class pair:
    def __init__(self,l_side,r_side):
        self.left_side=l_side
        self.right_side =r_side
        self.count = 1
    def get_pair(self):
        return self.right_side,self.right_side
    def get_count(self):
        return self.count
    def plus_one(self):
        self.count+=1
    def get_l_side(self):
        return self.left_side

from operator import attrgetter
def pair_func(arr,n):
    my_lst=[]
    for i in range(n-1):
        my_lst.append(pair(arr[i],arr[i+1]))
    my_lst.sort(key=attrgetter('left_side'))
    b = []
    l= len(my_lst)
    i=0
    max = 0
    while(i<l-1):
        if(my_lst[i].get_pair() == my_lst[i+1].get_pair()):
            my_lst.remove(my_lst[i+1])
            my_lst[i].count +=1
            l=len(my_lst)
        if(my_lst[i].count > max):
            max = my_lst[i].count
        else:
            i+=1


    for obj in my_lst:
        if max == obj.count:
            b.append(obj)
        # print(f'({obj.left_side},{obj.right_side},{obj.count})')
    return b

if __name__ == '__main__':

    arr = [4,5,7,88,2,3,4,5,2,3]
    my_lst =pair_func(arr,len(arr))
    for obj in my_lst:
        print(f'({obj.left_side},{obj.right_side},{obj.count})')








    sum1 = 0
    k=953
    arr_prime = sum_of_prime_number_equal_to_k(k)
    print(arr_prime)
    for i in arr_prime:
        sum1 += i
    if sum1 == k:
        print(f'{sum1}={k} ,the mission done')


    print('candidate:' ,find_the_mojority_element_in_arr([2,3,4,5,3,3]))


    print("result = " ,check_if_is_prime_num(187))

    a = [4,7,9,12,5,34,6,-2,67,1,45,-102,345,3,6,8,8,2354,6,323,3,6,22,4,66,7,8,3,21,6734,2345234,467,-23524356]
    print(find_min_max_A(a,len(a)))
    print(find_min_max_B(a,len(a)))

    arr=[1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
    n = len(arr)
    print(find_the_t_A(arr,n))
    print(find_the_t_B(arr,n))
    print(find_the_t_C(arr,n))


    matrix = [[2,0,1,0,0],[1,2,1,1,0],[0,0,2,0,0],[1,1,1,2,1],[0,0,1,1,2]]
    print("result = " ,find_the_star_fast(matrix,5))

    arr2 = [4,6,2,1,5]
    print(find_the_missing(arr2,6))
    sum = 0
    for i in range(100,1000):
        sum+=1

    print("sum =",sum)






# See PyCharm help at https://www.jetbrains.com/help/pycharm/

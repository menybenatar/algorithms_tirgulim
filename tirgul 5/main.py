# -----------------targil SELECT --------------------------------------------
# partition of quick sort
# ----------------------
def partition(arr, low, high):
    i = (low - 1)  # index of smaller element
    pivot = arr[high]  # pivot
    for j in range(low, high):

        # If current element is smaller than or
        # equal to pivot
        if arr[j] <= pivot:
            # increment index of smaller element
            i = i + 1
            arr[i], arr[j] = arr[j], arr[i]

    arr[i + 1], arr[high] = arr[high], arr[i + 1]
    return (i + 1)



def quickSort(arr, low, high):
    if len(arr) == 1:
        return arr
    if low < high:
        # pi is partitioning index, arr[p] is now
        # at right place
        pi = partition(arr, low, high)

        # Separately sort elements before
        # partition and after partition
        quickSort(arr, low, pi - 1)
        quickSort(arr, pi + 1, high)


# מציאת האיבר הK (אינקדס )בגודלו במערך .בזמן ריצה O(N)
def select (arr, low ,high ,k):
    if low == high:
        return low
    pivot = partition(arr,low,high)
    if (low < high):
        if (k == pivot):
            return pivot
        if (k < pivot):
            return select(arr, low, pivot - 1, k)
        else:
            return select(arr, pivot + 1, high, k)




def swap(arr,i,j):
   arr[i],arr[j] = arr[j],arr[i]


def median (arr,low,high,k):
    m = select(arr,low,high,(high-low+1)//2)
    return m



# שאלה 1 - מיין מערך ללא איבר שנמצא במקום הK
def sort_arr_without_k(arr,n,k):
   swap(arr,k,n)
   quickSort(arr,0,n-1)
   last = arr[n]
   for i in range(n,k,-1):
       arr[i] =arr[i-1]
   arr[k] = last
   print(arr)


# שאלה 2 - פונקצית חציון נתונה כקופסא שחורה , מצא את האיבר ה k הקטן ביותר בזמן לינארי O(N)
def select_by_median (arr,low,high,k):
    m = median(arr,low,high,k)
    # print(arr,m)
    if m == k:
        return arr[m]
    if (k < m):
        return select_by_median(arr, low, m-1, k)
    else:
        return select_by_median(arr, m+1 ,high ,k)



#   שאלה 3 -מציאת K איברים הקרובים לחציון
def find_k_element_clooser_to_median(arr,n,k):
    m = select(arr,0 ,n,(n+1)//2)
    diff=[]
    for i in range(n+1):
        diff.append(arr[i]-arr[m])
    dist_k = select(diff,0,n,k)
    for i in range(k):
        print(diff[i]+arr[m])

# שאלה 4 -ציונים A
def find_median_of_greads_A(arr,m,g_oll,g_new):

    if(g_oll  >  arr[m] and g_new > arr[m]):
        return arr[m]
    if (g_oll < arr[m] and g_new < arr[m]):
        return arr[m]
    if(g_oll < arr[m] and g_new > arr[m]):
        return g_new if (g_new < arr[m+1]) else arr[m+1]
    if (g_oll > arr[m] and g_new < arr[m]):
        return g_new if (g_new > arr[m-1]) else arr[m-1]
# שאלה 4 -ציונים B
def find_median_of_greads_B(arr,m,g_oll,g_new):

    if(g_oll  >  arr[m] and g_new > arr[m]):
        return arr[m]
    if (g_oll < arr[m] and g_new < arr[m]):
        return arr[m]

    i = 0
    n = len(arr)
    if(g_oll  <  arr[m] and g_new > arr[m]):
        while (arr[i] < arr[m]):
            i += 1
        m_smaller = arr[i]
        for i in range(i + 1, n+1):
            if arr[i] < m_smaller and arr[i] > arr[m]:
                m_smaller = arr[i]

        return m_smaller


    # while (arr[i] > arr[m]):
    #     i += 1
    #     m_bigger = arr[m]
# שאלה 5 - להוסיף X שאנו במערך
def appned_elemnet(arr,x,n):
    m = select(arr,0,n,(n+1)//2)
    smaller_than_x = 0
    bigger_than_x = 0
    for i in arr:
        if i < x:
            smaller_than_x+=1
        if i > x:
            bigger_than_x+=1

    return abs(smaller_than_x-bigger_than_x)
import random




if __name__ == '__main__':

    arr1 = [-5,3,6,12,15]
    arr2 = [-12,-10,-6,-3,4,10]







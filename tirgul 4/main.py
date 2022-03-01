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


# Driver code to test above


c_chen = 0
def what (a,b,n):
    global c_chen
    c_chen += 1
    if n==0:
        return a
    if n ==1:
        return b

    return(what(a,b,n-1)*what(a,b,n-2))


# Function for nth fibonacci
# number - Dynamic Programming
# Taking 1st two fibonacci numbers as 0 and 1
FibArray = [0, 1]


# Function for nth fibonacci
# number - Space Optimisataion
# Taking 1st two fibonacci numbers as 0 and 1

def fibonacci(n):
    a = 0
    b = 1


    if n < 0:
        print("Incorrect input")

    elif n == 0:
        return 0

    # Check if n is equal to 1
    elif n == 1:
        return b
    else:
        for i in range(1, n):
            c = a + b
            a = b
            b = c
            # print(b)
        return b


# Driver Program
print(str(fibonacci(10)))

def F():
    a,b = 0,1
    while True:
        yield a
        a, b = b, a + b


arr_fib = [-1 for i in range(50)]
def fib_loop(n):
    arr_fib[0] = 1
    arr_fib[1] = 1
    for i in range(2,n+1):
        arr_fib[i] = arr_fib[i-1]+arr_fib[i-2]
    return arr_fib[n]

def longest (a1,a2):
    res = ""
    for i in a1:
        if (i not in res):
            res+=i
    for i in a2:
        if (i not in res):
            res += i
    s = "".join(sorted(res))
    return s
def dorin(str):
    res = ""
    n = len(str)
    for i,j in zip(str,range(1,n+1)):
        for k in range(j):
            if k == 0:
                res += i.upper()
            else:
                res += i.lower()
        if j < n:
            res+='-'
    return res

# def create_phone_number(n):
#     s ="".join(str(a)for a in n)
#     return f'({s[:3]}) {s[3:6]}-{s[6:10]}'
def create_phone_number(n):
    return "({}{}{}) {}{}{}-{}{}{}{}".format(*n)



# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print(create_phone_number([1,2,3,4,5,6,7,8,9,0]))

    # print(longest("abcdefghijklmnopqrstuvwxyz",'abcdefghijklmnopqrstuvwxyz'))
    # what(2, 3, 20)
    print(dorin('abcd'))
    # print(c_chen)
    # print(fib_loop(7))
    #
    #
    #
    #
    #
    #
    #
    # arr = [10, 7, 8, 9, 1, 5]
    # n = len(arr)
    # quickSort(arr, 0, n - 1)
    # print("Sorted array is:")
    # for i in range(n):
    #     print("%d" % arr[i]),
    #



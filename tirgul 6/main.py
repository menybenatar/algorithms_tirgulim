
# --------------------------------------- תת סדרה מקסימלית ------------------
#  Naive solution O(n^2)
def maxSubArraySumNaive(arr,n):
    max_sum = max(0,arr[0])
    start =0; end =0

    for i in range(1,n):
        sum = 0
        for j in range(i,n):
            sum += arr[j]
            max_sum = max(max_sum,sum)


    return max_sum
#  Kanade algorithm  O(n) , place O(N)
def maxSubArraySumKanade(arr, n):
    sol =[]
    sol.append(arr[0]); max_sum = max(0,arr[0])

    for i in range(1, n):
        sol.append(max(arr[i],sol[i-1] +arr[i]))
        max_sum = max(max_sum,sol[i])

    return max_sum
#  Kanade algorithm  O(n) , place O(1)
def maxSubArraySumKanade(arr, n):
    s = arr[0]; max_sum = max(0,arr[0])
    for i in range(1, n):
        s = max(arr[i],s +arr[i])
        max_sum = max(max_sum,s)
    return max_sum

def maxSubArraySumKanade(arr, n):
    s = max_sum = 0
    i_max = j_max = -1
    i_last = 0
    for i in range(n):
        s = s +arr[i]
        if( s > max_sum):
            max_sum = s
            i_max = i_last
            j_max = i
        else:
            if s< 0:
                s =0
                i_last = i+1

    return max_sum,i_max,j_max
# ----------------------   EDIT DISTANCE ------------------
#  Naive solution RECRSIVE O(n^2)
def edit_distance(str1,str2,len1,len2):
    if(len1 == 0 and len2 == 0):
        return 0
    if(len1 == 0):
        return len2
    if (len2 == 0):
        return len1
    if(str1[len1] == str2[len2]):
        return edit_distance(str1,str2,len1-1,len2-1)
    else:
        return 1+min(edit_distance(str1,str2,len1-1,len2-1)+1,edit_distance(str1,str2,len1-1,len2),edit_distance(str1,str2,len1,len2-1))
# ----------------------   LEVENSHTEIN DISTANCE ------------------
#  dynamic solution  O(n^2)
def levenshteinDistance(str1,str2):
    len1 =len(str1)+1
    len2 =len(str2)+1
    mat = [ [0 for i in range(0,len2) ] for j in range(0,len1) ]
    for i in range(len1):
        mat[i][0] = i
    for j in range(len2):
        mat[0][j] =j


    for i in range(1,len1):
        for j in range(1,len2):
            if str1[i-1] == str2[j-1] :
                mat[i][j] = mat[i-1][j-1]
            else:
                mat[i][j] = 1 + min (mat[i-1][j-1], mat[i-1][j] ,mat[i][j-1] )

    for line in mat:
        print('  '.join(map(str, line)))
    return mat[i-1][j-1]
import math
def w(a,b,n):
    if n == 0:
        return a
    if n ==1 :
        return b
    return (w(a,b,n-1)*w(a,b,n-2))

t = w(2,2,10) ;count = 0
print(t)
while t>1:
    t = t/2
    count += 1
print(count)





if __name__ == '__main__':
    a = [3,-7,5,-4,5,1,-8,4]
    print(maxSubArraySumKanade(a, len(a)))

    str1 = "vintner"
    str2 = "writers"

    print(levenshteinDistance(str1,str2))

# mylist = []; my2list = []; strforappend= ''
# for i in range(100,999):
#     for j in range(100,999):
#         numstr = str(i*j)
#         if numstr == numstr[::-1]:
#             strforappend = f'{numstr}={i}*{j}'
#             mylist.append(i*j)
#             my2list.append(strforappend)
# mylist.sort()
# my2list.sort()
# print(mylist[-1])
# print(my2list)


n = 33
x='sg'
for i in range(0,n):
    for j in range(i,n):
        if j == i:
            print(' '* i,end='')
        print(f'{x} ', end='')
        if (j == n-1):
            print()




# See PyCharm help at https://www.jetbrains.com/help/pycharm/

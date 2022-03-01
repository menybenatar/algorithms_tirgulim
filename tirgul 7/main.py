# ================================== בעיית התרמיל ===================
# פתרון נאיבי רקורסיבי
def knapsacks_problem_rec(a,n,w):
    if w == 0:
        return 0
    if n < 0:
        return 0
    if a[n]['w'] >= w :
        return knapsacks_problem_rec(a,n-1,w)
    else:
        return max(knapsacks_problem_rec(a,n-1,w-a[n]['w']) + a[n]['b'] , knapsacks_problem_rec(a,n-1,w))
# פתרון דינמי
def knapsacks_problem_dynamic(a,n,w):
    mat =[['' for j in range(w+1)] for i in range(n+1)]
    for j in range(w+1):
        mat[0][j] = 0

    for i in range(n+1):
        mat[i][0] = 0

    for i in range(1,n+1):
        for j in range(1,w+1):

            if (a[i-1]['w'] <= j):
                if a[i-1]['b']+mat[i-1][j-a[i-1]['w']] > mat[i-1][j]:
                    mat[i][j] = a[i-1]['b'] + mat[i-1][j-a[i-1]['w']]
                else:
                    mat[i][j] = mat[i-1][j]
            else:
                mat[i][j] = mat[i-1][j]

    find_sol_knapsacks_problem(mat,n,w,w,a)
    return mat[n][w]
def find_sol_knapsacks_problem(mat,row,col,m,a):

    while m > 0:
      if mat[row][col] != mat[row-1][col]:
          print(a[row-1])
          col = col - a[row-1]['w']
          m = m - a[row-1]['w']
      row = row - 1


# =========================== subset sum problem - SSP ===================
# פתרון נאיבי רקורסיבי
def subset_sum_problem_rec(a,n,s):
    if s == 0:
        return 1
    if n < 0 and s != 0:
        return 0
    if a[n] > s:
        return subset_sum_problem_rec(a,n-1,s)
    else:
        return max(subset_sum_problem_rec(a,n-1,s) ,subset_sum_problem_rec(a,n-1,s-a[n]))


# פתרון דינמי
def subset_sum_problem_dyn(a,n,s):

    mat =[['' for j in range(s+1)] for i in range(n+1)]

    for i in range(n+1):
        mat[i][0] = 1
    for j in range(1,s+1):
        mat[0][j] = 0
    for i in range(1, n + 1):
        for j in range(1, s + 1):
            if a[i-1]> j:
                mat[i][j] = mat[i-1][j]
            else:
                mat[i][j] = max(mat[i-1][j],mat[i-1][j-a[i-1]])
    if mat[n][s]==1:
        print_path(a,mat,n+1,s+1)

    return mat

def print_path(a,mat ,row,col):
    i=row-1
    j=col-1
    while j!=0:
        if mat[i-1][j] ==0 :
            print(f'element :{a[i-1]}')
            j-=a[i-1]
        i-=1



def partition_problem(a,n):
    sum = 0
    for i in a:sum+=i
    if sum %2 == 1:
        return 0
    else:
        return subset_sum_problem_rec(a,n,sum/2)

# ================ משחק תרגיל DP3  ==================
def gemeRec(a,i,j):
    if i>j:
        return 0
    if i ==j :
        return a[i]
    if i+1 ==j :
        return max(a[i],a[j])

    res1 = a[i] + min (gemeRec(a,i+2,j) ,gemeRec(a,i+1,j-1))
    res2 = a[j] + min (gemeRec(a,i+1,j-1) ,gemeRec(a,i,j-2))
    return max(res1,res2)

def gemedynyulia(a,n):
    c = [['-1' for j in range(n)] for i in range(n)]
    for i in range(n):
        c[i][i] =a[i]

    for i in range(n-2,-1,-1):
        for j in range(i+1,n):
            c[i][j] = max(a[i]-c[i+1][j],a[j]-c[i][j-1])
    return c[0][n-1]

print('result = ',gemedynyulia([3,6,10,5],4))


def gemeDyn(a,n):
    mat = [['0' for j in range(n)] for i in range(n)]
    for i in range(n):
        for j in range(n):
            if i ==j:
                mat[i][j] = a[i]
            if i > j :
                mat[i][j] = 0

    for i in range(n):
        for j in range(n):
            if i<j:
                if (i + 2) <= j :
                    x = mat[i + 2][j]
                else :x =0
                if (i + 1) <= (j - 1) :
                    y = mat[i + 1][j - 1]
                else :y =0
                if i <= (j - 2) :
                    z = mat[i][j - 2]
                else :z =0
                mat[i][j] = max(a[i] + min(x, y), a[j] + min(y, z))


    for i in mat:
        print(i)


# ============= בעיית המטבעות ===============
import sys


# m is size of coins array (number of different coins)
def minCoins(coins, m, k):
    # base case
    if (k == 0):
        return 0

    # Initialize result
    res = sys.maxsize

    # Try every coin that has smaller value than V
    for i in range(0, m):
        if (coins[i] <= k):
            sub_res = minCoins(coins, m, k - coins[i])

            # Check for INT_MAX to avoid overflow and see if
            # result can minimized
            if (sub_res != sys.maxsize and sub_res + 1 < res):
                res = sub_res + 1

    return res


# =============  פתרון דינמי בזמן ריצה O(MK) ,סיבוכיות מקום O(K) ===============
def minCoins_dyn(coins, m, k):
    table = [sys.maxsize for i in range(k+ 1)]
    table[0] = 0


    for i in range(k+ 1):

        for j in range(m):

            if coins[j] <= i:
                temp = table[i-coins[j]]
                table[i] = min(temp + 1 ,table[i])

    if table[k] == sys.maxsize:
        return -1
    # print_path_coins(coins,m,table,k)

    return table[k]
# ======================  אלגוריתם לשחזור הפתרון  ===============
def print_path_coins(coins,m,table,k):
    j = 1
    while k != 0:
        for i in range(m):
            temp = table[k-coins[i]]
            if temp < table[k]:
                print(f'coin number {j} = {coins[i]}')
                j += 1
                k = k-coins[i]




# ==================== dorin problem =====================
import random
import string
def get_family_name():
    s = input("enter your family name:")
    if len(s)>4:
        return s[:4]
    return s

def get_random_lower_case(lower_case_size):
    letters = string.ascii_lowercase
    return ''.join(random.choice(letters) for i in range(lower_case_size))
def get_random_upper_case(upper_case_size):
    letters = string.ascii_uppercase
    return ''.join(random.choice(letters) for i in range(upper_case_size))
def get_random_digits(digits_size):
    letters = string.digits
    return ''.join(random.choice(letters) for i in range(digits_size))
def get_symbol(digits_size):
    letters = string.punctuation
    return ''.join(random.choice(letters) for i in range(digits_size))

def chek_if_name_in_pass(password,name):
    return name in password.lower()


def get_random_password(s_up,s_low,s_digit,s_symbol):
    four_last_name = get_family_name()
    password = ""
    i = 0
    while len(password) <13 :
        upper_case = get_random_upper_case(s_up+i)
        lower_case = get_random_lower_case(s_low+i)
        digit = get_random_digits(s_digit+i)
        symbol = get_symbol(s_symbol+i)
        password += lower_case+upper_case+digit+symbol
        i+=1
        while chek_if_name_in_pass(password,four_last_name):
            l = list(password)
            random.shuffle(l)
            password = ''.join(l)
    print(f'the password is : {password} ')

# get_random_password(5,3,3,2)
#==========================================================

# ========================== בעיית התרמיל תכנון דינמי שאלה מספר 4 ==============================
def lps_rec(s,i,j):
    if i ==j:
        return 1
    if s[i] == s[j]:
        return 2+lps_rec(s,i+1,j-1)
    else:
        return max(lps_rec(s,i+1,j),lps_rec(s,i,j-1))
def lps_dy(s):
    n =len(s)
    mat = [[ 0 for j in range(n)] for i in range(n)]
    for i in range(n):
        mat[i][i] = 1

    for diff in range(2,n+1): # רץ על אורך של מחרוזות לבדיקת פולינדרום
        for row in range(0,n-diff+1):
            col = row + diff -1
            if diff == 2 and s[row] == s[col]:
                mat[row][col] = 2
            elif s[row] == s[col]:
                mat[row][col] = 2 + mat[row+1][col-1]
            else:
                mat[row][col] = max(mat[row][col-1],mat[row+1][col])

    return mat[0][n-1]


# ==================== תת סדרה רציפה מקסימלית=============
#  הפונקציה מחזירה את הסדרה הרציפה המקסימלית המסתיימת בAi

def find_max_continuous_sub_seriesA(a,n):
    if n == 0:
        s=a[0]
        max_sum=max(0,s)
        return s,max_sum
    s_temp,max_sum_temp = find_max_continuous_sub_seriesA(a,n-1)
    s = max(a[n],s_temp+a[n])
    max_sum =max(max_sum_temp,s)
    return s,max_sum
def find_max_continuous_sub_seriesB(a,n):
    s=[a[0]]
    max_sum=max(0,s[0])
    for i in range(1,n):
        s.append(max(a[i],s[i-1]+a[i]))
        max_sum=max(max_sum,s[i])

    return max_sum
a=[-3,5,2,-2,-4,1,-6,3,-4]
print('res =',find_max_continuous_sub_seriesB(a,len(a)-1))



def find_sub_series_with_diff_1(a,n):
    s = [-1 for i in range(n)]
    s[0] = 1
    res = -1
    for i in range(1,n):
        max = 1
        for j in range(i):
            if abs(a[i] - a[j]) == 1 and max <= s[j]:
                max = s[j] + 1
        s[i] = max
        if res < max :
            res = max

    find_sol_sub_series_with_diff_1(a,n,s,res)
    return res
def find_sol_sub_series_with_diff_1(a,n,s,max):
    i = s.index(max)
    while max > 0:
        for j in range(i-1,0,-1):
            if abs (a[i]-a[j]) == 1  and s[i]-s[j] ==1:
                print(a[i])
                i=j
                break

        max-=1
    print(a[i])



arr =[3,-1,7,0,2,5,-2,1,-3,-2,4]
print('resultccc = ',  find_sub_series_with_diff_1(arr,len(arr)))



if __name__ == '__main__':
    s ="BBCBABACB"
    s=s+s+s+s+s+s
    print(s)
    print(lps_rec(s,0,len(s)-1))
    print(lps_dy(s))
    y= 'a;a;a;'
    p ={x:x*x for x in range(1,100)}
    print(p)
#     l = list("menybenatar")
#     random.shuffle(l)
#     result = ''.join(l)
#     print(result)

    # coins = [1,4,6]
    # m = len(coins)
    # k = 99999999
    # print("Minimum coins required is", minCoins_dyn(coins, m, k))

    # a =[{'w' :4, 'b' : 20},
    #     {'w' :2, 'b' : 3},
    #     {'w' :2, 'b' : 6},
    #     {'w' :6, 'b' : 25},
    #     {'w' :2, 'b' : 80}]
    # print(a[3]['b'])
    # n = len(a)-1
    # knapsacks_problem_rec(a,n,9)

    b = [{'w': 2, 'b': 3},
         {'w': 3, 'b': 4},
         {'w': 4, 'b': 5},
         {'w': 5, 'b': 6},]
    print(knapsacks_problem_dynamic(b, len(b)-1, 9))
    # print(alg1_dynamic(b, len(b)-1, 5))
    # mat = alg1_dynamic(a,len(a),9)
    # for i in mat: print(i)

    # c = [7,5,19,1,12,8,14]
    # print(subset_sum_problem_rec(c,len(c)-1,11))

    # d = [2, 1, 13, 5, 3, 21]
    # mat1 =subset_sum_problem_dyn(d, len(d) , 36)
    # for i in mat1: print(i)

    # e = [3,6,1,9,4,11]
    # print(partition_problem(c, len(e) - 1))
    # print(gemeRec([3,6,10,5] ,0, 3))
    # gemeDyn([3,6,10,5],4)


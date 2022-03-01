# This is a sample Python script.

# shufflin array
# סך כל התמורות של בניית מערך רנדומלי
# 1/n!
import random
import numpy as np
import datetime as t
import random as rd
def shaffling_arr(arr,n):
    return_arr =[]
    for i in range(n-1,-1,-1):
      index = rd.randint(0,i)
      return_arr.append(arr[index])
      arr[index] = arr[i]
    return return_arr

#חיפוש בתוך מערך גישה דטרמניסטית
def find_num_in_arr(arr,n,num):
    for i in range(n):
        if(num == arr[i]):
            return i
    return -1

# גישת מונטה קרלו למציאת איבר במערך עם הגרלה בתוחלת נמוכה

def find_monte_carlo_alg(arr,n,val):
    index_arr = [i for i in range(n)]
    for i in range(n-1,-1,-1):
        pos = rd.randint(0,i)
        print("pos=",pos)
        if(arr[index_arr[pos]] == val):
            return index_arr[pos]
        else:
            temp = index_arr[i]
            index_arr[i] = index_arr[pos]
            index_arr[pos] = temp
    return -1

# חישוב PAI

def pi(n):
    count = 0
    for i in range(1,n+1):
        x = rd.random()
        y = rd.random()
        if(x*x+y*y<=1):
            count+=1
    return 4*count/n


def print_prine_numbers(n):

    my_circul = [['.' for x in range(n)] for y in range(n)]
    a = n//2
    b = n//2
    r = n//2
    epsilon = 1.04
    print(a,b,r,epsilon)
    for x in range(n):
        for y in range(n):
            if abs((x-a) ** 2 + (y-b) ** 2 - r ** 2 ) < epsilon**2 : my_circul[x][y] = '#'



    for i in range(n):
        for j in range(n):
            print(my_circul[i][j] ,end=' ')
        print('')

def multipy_two_matrix_n_on_n(A,B,n):
    result = [[0 for x in range(n)] for y in range(n)]

    # iterating by row of A
    for i in range(len(A)):

        # iterating by column by B
        for j in range(len(B[0])):

            # iterating by rows of B
            for k in range(len(B)):
                result[i][j] += A[i][k] * B[k][j]

    return result
# כפל מטריצות
def check_if_vector_is_lier(AB,C,vector):

    ab= np.array(AB)
    c= np.array(C)
    y = np.array(vector)
    aby = ab.dot(y)
    cy = c.dot(y)
    print(f"AB*y  = {aby}")
    print(f"C*y  = {cy}")

    if not np.array_equal (ab , c) and np.array_equal (aby , cy):
        return 1


    else:
        return 0
def print_10_prime_number():
    a = int(input("enter num"))
    count = 0
    for i in range(a,1000000000000000000000000000000):
        if prime_num(i) == true:
         print(i)
         count+=1
         if (count == 10):
                return


if __name__ == '__main__':

    '''
    print_prine_numbers(5)
    arr =[1,2,3,4]
    n = 4
    arr2 = (shaffling_arr(arr,n))
    #print(find_monte_carlo_alg([1,2,3,4,5,6,7,8,9,10],10,3))
    print(t.datetime.now())
    print(pi(1000))
    print(t.datetime.now())'''

    AB = multipy_two_matrix_n_on_n([[1,1,1],[2,1,1],[1,2,2]],[[1,2,3],[1,3,1],[1,2,1]],3)
    print(AB)
    C =[[3,7,5],[10,3,8],[5,12,9]]
    print(C)
    if(AB!=C):
        print("not equal")
    else:
        print("equal")
    print(check_if_vector_is_lier(AB,C,[1,1,0]))


# See PyCharm help at https://www.jetbrains.com/help/pycharm/

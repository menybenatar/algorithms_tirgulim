# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


#question 1 in tirgul 2
#o(n)
def if_pten_is_premotaztia_in_txt(txt,ptrn):
    monim = [0 for x in range(27)]
    m = len(ptrn)
    n = len(txt)
    #o(m)

    for i in ptrn:
        if(i.isalpha()):
          monim[ord(i.lower()) - 97]+=1

    # o(m)
    for j in txt:
        if (j.isalpha()):
            monim[ord(j.lower()) - 97] -= 1
    # o(26)
    for i in monim:
        if i > 0:
            return False

    return True

#question 2 in tirgul 2
#o(n)
def risha_fun_of_kmp(ptrn):
    i =1
    j =0
    size = len(ptrn)
    lsp = ['?' for x in range(size)]

    lsp[0] = 0

    while(i < size):
        if(ptrn[i] == ptrn[j]):
            lsp[i] = j+1
            j+=1
            i+=1

        else:

            if(j == 0):
                lsp[i] = 0
                i+=1
            else:
                j =lsp[j-1]


    return lsp



def KMPSearch(txt,pat):
    M = len(pat)
    N = len(txt)

    # create lps[] that will hold the longest prefix suffix
    # values for pattern
    lps = [0] * M
    j = 0  # index for pat[]
    result = list()

    # Preprocess the pattern (calculate lps[] array)
    computeLPSArray(pat, M, lps)
    flag = 0
    i = 0  # index for txt[]
    while i < N:
        if pat[j] == txt[i]:
            i += 1
            j += 1

        if j == M:
            #print("Found pattern at index " + str(i - j))
            result.append(i-j)
            j = lps[j - 1]
            flag = 1

        # mismatch after j matches
        elif i < N and pat[j] != txt[i]:
            # Do not match lps[0..lps[j-1]] characters,
            # they will match anyway
            if j != 0:
                j = lps[j - 1]
            else:
                i += 1

    if flag:
        return result
    else:
        return False
def computeLPSArray(pat, M, lps):
	len = 0 # length of the previous longest prefix suffix
	lps[0] # lps[0] is always 0
	i = 1

	# the loop calculates lps[i] for i = 1 to M-1
	while i < M:
		if pat[i]== pat[len]:
			len += 1
			lps[i] = len
			i += 1
		else:
			# This is tricky. Consider the example.
			# AAACAAAA and i = 7. The idea is similar
			# to search step.
			if len != 0:
				len = lps[len-1]

				# Also, note that we do not increment i here
			else:
				lps[i] = 0
				i += 1


#question 3 in tirgul 2
#o(n)
def two_string_is_Circular_rotation(t1,t2):
    temp = t1 *2
    res = KMPSearch(temp,t2)
    if res:
        print("The strings are a circular rotation")
    else:
        print("The strings are NOT a circular rotation")



#question 4 in tirgul 2
def alg_to_find_divition(txt):
    lps = risha_fun_of_kmp(txt)
    print(lps)
    n = len(txt)
    k = lps[n-1]
    while(k > ((n-10)/2)-1):
        k = lps[k]
    x = txt[0:k]
    y = txt[k:n-k]
    return x,y,x
#question 5 in tirgul 2
def alg_to_find_bigger_risha_is_polindrom(txt):
    txt_r = txt[::-1]
    lps = risha_fun_of_kmp(txt+txt_r)
    print((lps))
    n = len(txt+txt_r)
    k = lps[n-1]

    while(k > n):
        k = lps[k]
    poli_of_dorin= txt[:k]
    return poli_of_dorin




#question 8 in tirgul 2
def find_position_of_k_patterns_in_text(text,patrs):
    my_dict = dict()
    for i in patrs:
        res = KMPSearch(text,i)
        if res:
            my_dict[i] = res
        else :
            my_dict[i] =[]
    return my_dict

import random
from numpy import random as rn
import numpy as dorin
if __name__ == '__main__':

     ptr = "ababbaabca"
     print(risha_fun_of_kmp(ptr))
     ptr ="dorin"
     p = ""
     for x in range(0,5,2):
         p += ptr[x]
     print(p)

     d = rn.randint(7,55)
     s = dorin.zeros(9)
     print(s)


'''
    p1 = "CAR"
    p2 = "ARC"
    two_string_is_Circular_rotation(p1, p2)
    patterns = ['yet','way','in','the']

    print(find_position_of_k_patterns_in_text(text,patterns))





    text = "menybenafgjedgashrafgjtzsfAHJFAdghdfq4576uq    15qheafada 4wthae fhkgh34576   3576efdsh tar"
    pattern = "rafgjtz"
    print(if_pten_is_premotaztia_in_txt(text,pattern))
    
   
'''





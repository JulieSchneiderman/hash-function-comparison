import math
#Assignment 3
#Julie Schneiderman - 10201092
#I confirm that this submission is my own work and is consistent with the Queen's regulations on Academic Integrity.


#takes in .txt file and list of prime numbers
#creates list of varying size initialized to None
#loops through .txt file to find table sizes that result in collisions
#outputs table sizes that fail the 'cannot look at more than 10 locations' requirement
def func1(codenames, m):
    for num in m:
        #print("num-------------",num)
        A = [None] * num #create empty list of size num - all values initialized to 'None' [None, None.....num-1]
        codenames = open("codenames", "r")
        #print(codenames) #test
        #print(len(A)) #test

        max_collisions = 0

        #print("num = ",num)
        #print("len(A) = ",len(A))
        
        for word in codenames.readlines():
            #print(word) #test
            collisions = quadratic_probing_insert(A,word) #switch to quadratic_probing_insert(A,word) to do that experiment
            if collisions > max_collisions:
                max_collisions = collisions
        if max_collisions > 10:
            print("fails for table size equal to: ", num, "  -- num collisions: ", max_collisions)
        else:
            print("success for table size equal to: ",num," -- num collisions: ", max_collisions )


#Algorithm from Dawes notes on March 6th
#input codename
#S[:-1] because last value of each word is \n which would increase the value of a by 10 (ord("\n") = 10)
#output int value for that codename
def codenames_to_int(s):
    a = 0
    for x in s[:-1]:
        a += ord(x)*(ord(x))
        #print(a) 
    #print('a=', a) 
    return (a) #key value

#------Quadratic Probing -----------#
#take in the 'None' list of size num and a word to be converted into an integer and then hashed
#returns the number of collisions that occured while attempting to insert a code word
def quadratic_probing_insert(T, w):
    #constants - (trial 1 = 1,2), (trial 2 = 1,2), (trial 3 = 2,1)
    c1 = 2
    c2 = 1 
    i = 0
    key = codenames_to_int(w) #sends to code name to integer converted, that value becomes the key value
    v = h(key,len(T)) #value returned as 'sum' => type int
    a = v
    while ((i<len(T)) and (T[a] != None)): #T[a] is already assignned - collision occured, increment i 
        i+=1
        a = (v + c1*i + (c2*(i*i))) % len(T)
    if(T[a] == None):
            T[a] = w
            #print("inserted ",w)
            
    #print(w)
    #print(i)
    return i

#hash function for quadratic probing -  mulitplication method
def h(k,num):
    V = (math.sqrt(5)-1)/2
    whole = math.floor(V*k) 
    x = V*k - whole #gives fractional part of number
    #print("hash func val: ", math.floor(num*x))
    return math.floor(num*x)


#----------Double Hashing-------------#
#h(k,i) = (h'(k) + i*h"(k)) mod m
def double_hashing_insert(T, w):
    i = 0
    key = codenames_to_int(w)
    v = h(key,len(T))
    v2 = h2(key)
    a = v
    while ((i<len(T)) and (T[a] != None)): #T[a] is already assignned - collision occured, increment i 
        i+=1
        #a = math.floor((v + (i*v) + (i*v2)) % len(T)) #trial 1
        a = math.floor((v + (i*v2) + (i*v)) % len(T)) #trial 2
        #a = math.floor((v + (i*v) + (i*v)) % len(T)) #trial 3
    if(T[a] == None):
            T[a] = w
    return i

#h''(k) function
#mid square method -- Dawes' notes March 6th
def h2(k):
    s = k*k
    x = s / 1000
    a = x % 1000
    return a


#reads in codenames text file, sends call to func1     
def main():
    m = list(range(3700,6000))
    codenames = open("codenames", "r")
    func1(codenames, m)


main()

# Python3 program to find all pairs in 
# a list of integers with given sum 

def findPairs(lst, K): 
    res = [] 
    while lst: 
        num = lst.pop() 
        diff = K - num 
        if diff in lst: 
            res.append((diff, num)) 
    return res 
	
# Driver code 
lst = [1, 5, 3, 7, 9] 
K = 12
print(len(findPairs(lst, K))) 

lst = [1,3,9,5,8,6,4]
K = 12
print(len(findPairs(lst, K))) 

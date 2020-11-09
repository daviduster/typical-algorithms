# DP approach for the knapsack problem
  

'''
Let weight elements = {1, 2, 3}
Let weight values = {10, 15, 40}
Capacity=6

   0   1   2   3   4   5   6

0  0   0   0   0   0   0   0

1  0  10  10  10  10  10  10

2  0  10  15  25  25  25  25

3  0
 
Explanation:
For filling 'weight = 2' we come 
across 'j = 3' in which 
we take maximum of 
(10, 15 + DP[1][3-2]) = 25   
  |        |
'2'       '2 filled'
not filled  


   0   1   2   3   4   5   6

0  0   0   0   0   0   0   0

1  0  10  10  10  10  10  10

2  0  10  15  25  25  25  25

3  0  10  15  40  50  55  65
'''

# A Dynamic Programming based Python  
# Program for 0-1 Knapsack problem 
# Returns the maximum value that can  
# be put in a knapsack of capacity W 
def knapsack_dp(C, wt, val, n): 
    K = [[0 for x in range(C + 1)] for x in range(n + 1)] 
  
    # Build table K[][] in bottom up manner 
    for i in range(n + 1): 
        for w in range(C + 1): 
            if i == 0 or w == 0: 
                K[i][w] = 0
            elif wt[i-1] <= w: 
                K[i][w] = max(val[i-1] + K[i-1][w-wt[i-1]],  K[i-1][w]) 
            else: 
                K[i][w] = K[i-1][w] 
  
    return K[n][C] 
  
# Driver program to test above function 
val = [60, 100, 120]  # values
wt = [10, 20, 30] # weights
C = 50 # Capacity
n = len(val) 
print(knapsack_dp(C, wt, val, n)) 
  


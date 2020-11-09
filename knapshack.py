# A naive recursive implementation 
# of 0-1 Knapsack Problem 
  
# Returns the maximum value that  
# can be put in a knapsack of  
# capacity W 

def knapSackRecursive(W, wt, val, n): 
  
    # Base Case 
    if n == 0 or W == 0 : 
        return 0
  
    # If weight of the nth item is  
    # more than Knapsack of capacity W,  
    # then this item cannot be included  
    # in the optimal solution 
    if (wt[n-1] > W): 
        return knapSackRecursive(W, wt, val, n-1) 
  
    # return the maximum of two cases: 
    # (1) nth item selected  val[n-1] + knapSack(W-wt[n-1], wt, val, n-1)
    # (2) not selected knapSack(W, wt, val, n-1)
    else: 
        return max( 
            val[n-1] + knapSackRecursive( 
                W-wt[n-1], wt, val, n-1),  
                knapSackRecursive(W, wt, val, n-1)) 
  
# end of function knapSack 
  
# To test above function 
val = [60, 100, 120] 
wt = [10, 20, 30] 
W = 50
n = len(val) 
print(knapSackRecursive (W, wt, val, n))
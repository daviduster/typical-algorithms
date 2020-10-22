# Python program to solve fractional Knapsack Problem


def fractional_knapsack(wt, val, capacity):
    ratios = {}

    zip_iterator =zip(val, wt)
    ratios = dict(zip_iterator)

    # sorts the item according to value/weight ratio in non-decreasing order
    ratios = dict(sorted(ratios.items(), key=lambda x: x[0] / x[1], reverse = True ))

    print(list(ratios.keys()))
    print(list(ratios.values()))

    max_val = 0
    for i in range(0,len(ratios)):
        current_val = list(ratios.keys())[i]
        current_wt =  list(ratios.values())[i]
        if capacity - current_wt >= 0:
            capacity -= current_wt
            max_val += current_val
        else:
            fraction = capacity / current_wt
            max_val += current_val * fraction
            capacity = int(capacity - (current_wt * fraction))
            break

    return max_val
    
wt = [10, 40, 20, 30]
val = [60, 40, 100, 120]
capacity = 50

# Function call
print("Maximum value in Knapsack =", fractional_knapsack(wt, val, capacity))
